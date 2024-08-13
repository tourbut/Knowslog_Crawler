from app.models import *
from app.src.schemas import archive as archive_schema
from sqlmodel import Session, select

async def create_archive(*,session: Session, archive: archive_schema.Archive,user_id:int) -> Archive:
    db_obj = Archive.model_validate(archive,update={"user_id":user_id})
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

async def get_archive(*,session: Session,user_id:int,archive_id:int) -> Archive:
    query = select(Archive).where(Archive.user_id == user_id,Archive.id == archive_id)
    archive = await session.exec(query)
    if archive is None:
        return None
    else:
        return archive.first()
    
async def get_archive_list(*,session: Session,user_id:int) -> Archive:
    query = select(Archive.id,
                   Archive.category,
                   Archive.title,
                   Archive.url).where(Archive.user_id == user_id)
    archive = await session.exec(query)
    if archive is None:
        return None
    else:
        return archive.all()

async def get_userllm(*, session: Session,user_id:int) -> UserLLM| None:
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