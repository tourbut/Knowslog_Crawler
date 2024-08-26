import uuid
from typing import Any,List

from fastapi import APIRouter, HTTPException

from app.src.deps import SessionDep_async,CurrentUser
from app.src.crud import chat as chat_crud
from app.src.schemas import chat as chat_schema
from fastapi.responses import StreamingResponse
from langchain_core.messages import AIMessageChunk
from app.core.config import settings
from app.src.engine.llms.chain import translate_chain,summarize_chain,chatbot_chain
from datetime import datetime
from requests.exceptions import RequestException

router = APIRouter()


@router.post("/send_message",response_model=chat_schema.OutMessage)
async def send_message(*, session: SessionDep_async, current_user: CurrentUser,chat_in: chat_schema.SendMessage):
    
    userllm = await chat_crud.get_llm(session=session,user_id=current_user.id,user_llm_id=chat_in.user_llm_id)
    
    messages = []
    user_message = chat_schema.CreateMessage(user_id=current_user.id,
                                             chat_id=chat_in.chat_id,
                                             name=current_user.name,
                                             content=chat_in.input,
                                             is_user=True)
    messages.append(user_message)
    
    async def chain_astream(input):
    
        chain = chatbot_chain(api_key=userllm.api_key,
                              model=userllm.name)
        
        chunks=[]
        
        async for chunk in chain.astream({'input':input}):
            chunks.append(chunk)
            yield chat_schema.OutMessage(content=chunk.content,
                                         input_token=chunk.usage_metadata['input_tokens'] if chunk.usage_metadata is not None else None,
                                         output_token=chunk.usage_metadata['output_tokens'] if chunk.usage_metadata is not None else None,
                                         is_done=False).model_dump_json()
            
        response=chunks[0]
        
        for chunk in chunks[1:]:
            response+=chunk
        print(response.content)
        
        
        bot_message = chat_schema.CreateMessage(user_id=current_user.id,
                        chat_id=chat_in.chat_id,
                        name="Knowslog Bot",
                        content=response.content,
                        is_user=False)
        
        messages.append(bot_message)

        
        await chat_crud.create_messages(session=session,messages=messages)
        
        yield chat_schema.OutMessage(content=response.content,
                                    input_token=response.usage_metadata['input_tokens'],
                                    output_token=response.usage_metadata['output_tokens'],
                                    is_done=True).model_dump_json()
        
    return StreamingResponse(chain_astream(chat_in.input),media_type='text/event-stream')

@router.post("/create_chat",response_model=chat_schema.ResponseChat)
async def create_chat(*, session: SessionDep_async, current_user: CurrentUser,chat_in: chat_schema.CreateChat):
    chat = await chat_crud.create_chat(session=session,current_user=current_user,title=chat_in.title,user_llm_id=chat_in.user_llm_id)
    return chat

@router.get("/get_chat_list",response_model=List[chat_schema.GetChat])
async def get_chat_list(*, session: SessionDep_async, current_user: CurrentUser):
    chats = await chat_crud.get_chat_list(session=session,current_user=current_user)
    return chats

@router.get("/get_messages",response_model=List[chat_schema.ReponseMessages])
async def get_messages(*, session: SessionDep_async, current_user: CurrentUser, chat_id:uuid.UUID):
    messages = await chat_crud.get_messages(session=session,current_user=current_user,chat_id=chat_id)
    return messages

@router.get("/get_userllm",response_model=List[chat_schema.GetUserLLM])
async def get_userllm(*, session: SessionDep_async, current_user: CurrentUser):
    userllm = await chat_crud.get_userllm(session=session,user_id=current_user.id)
    return userllm

@router.put("/delete_chat")
async def delete_chat(*, session: SessionDep_async, current_user: CurrentUser,in_chat:chat_schema.Update_Chat):
    
    in_chat.delete_yn = True
    
    chat = await chat_crud.update_chat(session=session,chat=in_chat)
    return {"message":"Chat deleted successfully"}