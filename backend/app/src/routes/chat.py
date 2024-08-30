import uuid
from typing import Any,List

from fastapi import APIRouter, HTTPException

from app.src.deps import SessionDep_async,CurrentUser,async_engine,engine
from app.src.crud import chat as chat_crud
from app.src.schemas import chat as chat_schema
from fastapi.responses import StreamingResponse
from app.core.config import settings
from app.src.engine.llms.chain import translate_chain,summarize_chain,chatbot_chain
from app.src.engine.llms.memory import pg_vetorstore_with_memory
from datetime import datetime
from requests.exceptions import RequestException
from langchain_redis import RedisChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
)
router = APIRouter()

REDIS_URL = settings.REDIS_URL

# Function to get or create a RedisChatMessageHistory instance
def get_redis_history(session_id: str) -> BaseChatMessageHistory:
    return RedisChatMessageHistory(session_id, redis_url=REDIS_URL)

@router.post("/send_message",response_model=chat_schema.OutMessage)
async def send_message(*, session: SessionDep_async, current_user: CurrentUser,chat_in: chat_schema.SendMessage):
    
    # Get userllm
    userllm = await chat_crud.get_llm(session=session,user_id=current_user.id,user_llm_id=chat_in.user_llm_id)
    
    # Get a postgres vectorstore with memory
    memory = pg_vetorstore_with_memory(connection=engine,
                                       collection_name=chat_in.chat_id.hex,
                                       api_key=userllm.api_key,
                                       model="text-embedding-3-large",
                                       search_kwargs={"k": 1})
    
    # Get or create a RedisChatMessageHistory instance
    history = get_redis_history(chat_in.chat_id.hex)
    
    user_message = chat_schema.CreateMessage(user_id=current_user.id,
                                             chat_id=chat_in.chat_id,
                                             name=current_user.name,
                                             content=chat_in.input,
                                             is_user=True)
    messages = []
    messages.append(user_message)
    
    async def chain_astream(input):
    
        chain = chatbot_chain(api_key=userllm.api_key,
                              model=userllm.name,
                              #get_redis_history=get_redis_history
                              memory=memory
                              )
        
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
        
        bot_message = chat_schema.CreateMessage(user_id=current_user.id,
                        chat_id=chat_in.chat_id,
                        name="Knowslog Bot",
                        content=response.content,
                        is_user=False)
        
        messages.append(bot_message)

        usage = chat_schema.Usage(user_llm_id=chat_in.user_llm_id,
                                  input_token=response.usage_metadata['input_tokens'],
                                  output_token=response.usage_metadata['output_tokens'])
        
        await chat_crud.create_messages(session=session,messages=messages,usage=usage)
        
        # Add messages to chat history
        await history.aadd_messages([HumanMessage(content=user_message.content,
                                                  additional_kwargs={
                                                      "user_id":str(user_message.user_id),
                                                      "name":user_message.name
                                                      }),])
        await history.aadd_messages([AIMessage(content=str(bot_message.content),
                                               additional_kwargs={
                                                   "user_id":str(bot_message.user_id),
                                                   "name":bot_message.name
                                                   })])
        
        memory.save_context(
            inputs={
                "human": user_message.content
                },
            outputs={
                "ai": bot_message.content
                },
            )
        
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
    history = get_redis_history(chat_id.hex)
    messages = await chat_crud.get_messages(session=session,current_user=current_user,chat_id=chat_id)
    return messages

@router.get("/get_userllm",response_model=List[chat_schema.GetUserLLM])
async def get_userllm(*, session: SessionDep_async, current_user: CurrentUser):
    userllm = await chat_crud.get_userllm(session=session,user_id=current_user.id)
    return userllm

@router.put("/delete_chat")
async def delete_chat(*, session: SessionDep_async, current_user: CurrentUser,chat_in:chat_schema.Update_Chat):
    history = RedisChatMessageHistory(session_id=chat_in.id.hex, redis_url=REDIS_URL)
    history.clear()
    chat_in.delete_yn = True
    
    chat = await chat_crud.update_chat(session=session,chat=chat_in)
    return {"message":"Chat deleted successfully"}

@router.get("/get_chat",response_model=chat_schema.GetChat)
async def get_chat(*, session: SessionDep_async, current_user: CurrentUser,chat_id:uuid.UUID):
    chat = await chat_crud.get_chat(session=session,chat_id=chat_id)
    return chat