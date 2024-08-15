from app.models import *
from app.src.schemas import archive as archive_schema
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

async def get_archive(*,session: AsyncSession,user_id:int,archive_id:int) -> Archive| None:
    query = select(Archive).where(Archive.user_id == user_id,Archive.id == archive_id)
    archive = await session.exec(query)
    if archive is None:
        return None
    else:
        return archive.first()
    
async def get_archive_list(*,session: AsyncSession,user_id:int) -> Archive:
    query = select(Archive.id,
                   Archive.category,
                   Archive.title,
                   Archive.url).where(Archive.user_id == user_id)
    archive = await session.exec(query)
    if archive is None:
        return None
    else:
        return archive.all()

async def get_userllm(*, session: AsyncSession,user_id:int) -> archive_schema.GetUserLLM| None:
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

async def create_archive(*,session: AsyncSession, archive: archive_schema.Archive,user_id:int) -> Archive:
    try:
        db_obj = Archive.model_validate(archive, update={"user_id":user_id})
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj
    except Exception as e:
        print(e)
        await session.rollback()
        raise e

async def create_refine(*,session: AsyncSession, refine: archive_schema.Refine) -> Refine| None:
    db_obj = Refine.model_validate(refine)
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

async def create_usage(*,session: AsyncSession, usage: archive_schema.Usage) -> UserUsage| None:
    db_obj = UserUsage.model_validate(usage)
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

async def create_archive_refine_usage(*,session: AsyncSession,
                                      archive: archive_schema.Archive, 
                                      refine: archive_schema.Refine, 
                                      usage: archive_schema.Usage,
                                      user_id:int) -> Archive:
    try:
        db_archive = None
        db_refine = None
        db_usage = None
        
        if archive:
            db_archive = Archive.model_validate(archive, update={"user_id":user_id})
            session.add(db_archive)
            await session.flush()
        if refine:
            db_refine = Refine.model_validate(refine, update={"user_id":user_id,
                                                              "archive_id":db_archive.id})
            session.add(db_refine)
        if usage:
            db_usage = UserUsage.model_validate(usage)
            session.add(db_usage)
        
        await session.commit()
        
        await session.refresh(db_archive) if archive else None
        await session.refresh(db_refine) if refine else None
        await session.refresh(db_usage) if usage else None
        
        return db_archive, db_refine, db_usage
    except Exception as e:
        print(e)
        await session.rollback()
        raise e