from typing import List
import uuid
from app.models import *
from app.src.schemas import chat as chat_schema
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_userllm(*, session: AsyncSession,user_id:uuid.UUID) -> List[chat_schema.GetUserLLM]| None:
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
        return userllm.all()

async def get_llm(*, session: AsyncSession,user_id:uuid.UUID,user_llm_id:uuid.UUID) -> chat_schema.GetUserLLM| None:
    statement = select(UserLLM.id,
                       LLM.source,
                       LLM.name,
                       UserAPIKey.api_key).where(UserLLM.user_id == user_id,
                                                   UserLLM.llm_id == LLM.id,
                                                   UserLLM.api_id ==UserAPIKey.id,
                                                   UserLLM.active_yn == True,
                                                   UserLLM.id == user_llm_id)
    userllm = await session.exec(statement)
    if not userllm:
        return None
    else:
        return userllm.first()

async def create_usage(*,session: AsyncSession, usage: chat_schema.Usage) -> UserUsage| None:
    db_obj = UserUsage.model_validate(usage)
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj
    
async def create_chat(*, session: AsyncSession, current_user: User,title:str,user_llm_id:uuid.UUID) -> Chats:
    chat = Chats(user_id=current_user.id,
                 title=title,
                 user_llm_id=user_llm_id)
    
    session.add(chat)
    await session.commit()
    await session.refresh(chat)
    return chat

async def create_messages(*, session: AsyncSession, messages:List[Messages]) -> Messages:
    
    for message in messages:
        db_obj = Messages.model_validate(message)
        session.add(db_obj)
    
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

async def get_messages(*, session: AsyncSession,current_user: User, chat_id:uuid.UUID) -> List[chat_schema.ReponseMessages]:
    statement = select(Messages).where(Messages.chat_id == chat_id,
                                       Messages.user_id == current_user.id,
                                       Messages.delete_yn == False)
    messages = await session.exec(statement)
    return messages.all()

async def get_chat_list(*, session: AsyncSession, current_user: User) -> List[chat_schema.GetChat]:
    statement = select(Chats).where(Chats.user_id == current_user.id,
                                    Chats.delete_yn == False)
    chats = await session.exec(statement)
    return chats.all()

async def update_chat(*,session: AsyncSession, chat: chat_schema.Update_Chat) -> Chats:
    db_chat = await session.get(Chats, chat.id)
    
    if not db_chat:
        return None
    else:
        update_dict = chat.model_dump(exclude_unset=True)
        db_chat.sqlmodel_update(update_dict)
        db_chat.update_date = datetime.now()
        session.add(db_chat)
        await session.commit()
        await session.refresh(db_chat)
    return db_chat
    