from typing import List
from app.models import *
from app.src.schemas import chat as chat_schema
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_userllm(*, session: AsyncSession,user_id:int) -> chat_schema.GetUserLLM| None:
    statement = select(UserLLM.id,
                       LLM.source,
                       LLM.name,
                       UserAPIKey.api_key).where(UserLLM.user_id == user_id,
                                                   UserLLM.llm_id == LLM.id,
                                                   UserLLM.api_id ==UserAPIKey.id,
                                                   UserLLM.active_yn == True)
    userllm = await session.exec(statement)
    if not userllm:
        return None
    else:
        return userllm.first()