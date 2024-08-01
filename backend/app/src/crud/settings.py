from typing import List
from app.models import *
from app.src.schemas import settings as settings_schema
from sqlmodel import Session, select

async def get_llm(*, session: Session) -> List[LLM]| None:
    statement = select(LLM)
    llm = await session.exec(statement)

    if not llm:
        return None
    else:
        return llm.all()
    
async def create_apikey(*, session: Session, apikey_in: settings_schema.Create_Apikey,user_id:int) -> UserAPIKey:
    db_obj = UserAPIKey.model_validate(apikey_in,update={"user_id":user_id})
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

async def get_apikey(*, session: Session,user_id:int) -> List[UserAPIKey]| None:
    statement = select(UserAPIKey).where(UserAPIKey.user_id == user_id)
    apikey = await session.exec(statement)
    if not apikey:
        return None
    else:
        return apikey.all()

async def update_apikey(*, session: Session, apikey_update: settings_schema.Get_Apikey) -> UserAPIKey:
    apikey = await session.get(UserAPIKey, apikey_update.id)
    
    if not apikey:
        return None
    else:
        update_dict = apikey_update.model_dump(exclude_unset=True)
        apikey.sqlmodel_update(update_dict)
        apikey.update_date = datetime.now()
        session.add(apikey)
        await session.commit()
        await session.refresh(apikey)

    return apikey


async def get_userllm(*, session: Session,user_id:int) -> List[UserLLM]| None:
    statement = select(UserLLM).where(UserLLM.user_id == user_id)
    userllm = await session.exec(statement)
    if not userllm:
        return None
    else:
        return userllm.all()
    
async def create_userllm(*, session: Session, userllm_in: settings_schema.Create_UserLLM,user_id:int) -> UserLLM:
    db_obj = UserLLM.model_validate(userllm_in,update={"user_id":user_id})
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj
