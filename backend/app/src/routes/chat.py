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
    
    userllm = await chat_crud.get_userllm(session=session,user_id=current_user.id)
    
    async def chain_astream(input):
    
        chain = chatbot_chain(api_key=userllm.api_key,
                              model=userllm.name)
        
        chunks=[]
        
        async for chunk in chain.astream({'input':input}):
            chunks.append(chunk)
            yield chat_schema.OutMessage(content=chunk.content,
                                         input_token=chunk.usage_metadata['input_tokens'] if chunk.usage_metadata is not None else None,
                                         output_token=chunk.usage_metadata['output_tokens'] if chunk.usage_metadata is not None else None,).model_dump_json()
            
        response=chunks[0]
        
        for chunk in chunks[1:]:
            response+=chunk
        
        yield chat_schema.OutMessage(content=response.content,
                                    input_token=response.usage_metadata['input_tokens'],
                                    output_token=response.usage_metadata['output_tokens'],).model_dump_json()
        
    return StreamingResponse(chain_astream(chat_in.input),media_type='text/event-stream')
            
            