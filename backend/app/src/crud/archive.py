import uuid

from typing import List
from app.models import *
from app.src.schemas import archive as archive_schema
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

async def get_archive(*,session: AsyncSession,user_id:uuid.UUID,archive_id:uuid.UUID) -> Archive| None:
    query = select(Archive).where(Archive.user_id == user_id,
                                  Archive.id == archive_id,
                                  Archive.delete_yn == False)
    archive = await session.exec(query)
    if archive is None:
        return None
    else:
        return archive.first()

async def get_refine(*,session: AsyncSession,user_id:uuid.UUID,archive_id:uuid.UUID) -> List[Refine]| None:
    query = select(Refine).where(Refine.user_id == user_id,
                                 Refine.archive_id == archive_id)
    refine = await session.exec(query)
    if refine is None:
        return None
    else:
        return refine.all()

async def get_archive_list(*,session: AsyncSession,user_id:uuid.UUID) -> Archive:
    query = select(Archive.id,
                   Archive.category,
                   Archive.title,
                   Archive.url).where(Archive.user_id == user_id,
                                      Archive.delete_yn == False)
    archive = await session.exec(query)
    if archive is None:
        return None
    else:
        return archive.all()

async def get_file_list(*,session: AsyncSession,user_id:uuid.UUID) -> UserFiles:
    query = select(UserFiles.id,
                   UserFiles.file_name,
                   UserFiles.file_size,
                   UserFiles.file_ext,
                   UserFiles.file_desc,
                   ).where(UserFiles.user_id == user_id,
                           UserFiles.delete_yn == False)
    files = await session.exec(query)
    if files is None:
        return None
    else:
        return files.all()

async def delete_file(*,session: AsyncSession,user_id:uuid.UUID,file_id:uuid.UUID) -> UserFiles| None:
    file = await session.get(UserFiles, file_id)
    if not file:
        return None
    else:
        file.delete_yn = True
        session.add(file)
        await session.commit()
        await session.refresh(file)
        return file

async def get_userllm(*, session: AsyncSession,user_id:uuid.UUID) -> archive_schema.GetUserLLM| None:
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

async def create_archive(*,session: AsyncSession, archive: archive_schema.Archive,user_id:uuid.UUID) -> Archive:
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
                                      refine_1: archive_schema.Refine, 
                                      usage_1: archive_schema.Usage,
                                      refine_2: archive_schema.Refine, 
                                      usage_2: archive_schema.Usage,
                                      user_id:uuid.UUID) -> Archive:
    try:
        db_archive = None
        db_refine_1 = None
        db_usage_1 = None
        db_refine_2 = None
        db_usage_2 = None
        
        if archive:
            db_archive = Archive.model_validate(archive, update={"user_id":user_id})
            session.add(db_archive)
            await session.flush()
            
        if refine_1:
            db_refine_1 = Refine.model_validate(refine_1, update={"user_id":user_id,
                                                              "archive_id":db_archive.id})
            session.add(db_refine_1)
            await session.flush()
        if usage_1:
            db_usage_1 = UserUsage.model_validate(usage_1)
            session.add(db_usage_1)
            await session.flush()
            
        if refine_2:
            db_refine_2 = Refine.model_validate(refine_2, update={"user_id":user_id,
                                                              "archive_id":db_archive.id})
            session.add(db_refine_2)
            await session.flush()
        if usage_2:
            db_usage_2 = UserUsage.model_validate(usage_2)
            session.add(db_usage_2)
            await session.flush()
        
        await session.commit()
        
        await session.refresh(db_archive) if archive else None
        await session.refresh(db_refine_1) if refine_1 else None
        await session.refresh(db_usage_1) if usage_1 else None
        await session.refresh(db_refine_2) if refine_2 else None
        await session.refresh(db_usage_2) if usage_2 else None
        
        return db_archive, db_refine_1, db_usage_1, db_refine_2, db_usage_2
    except Exception as e:
        print(e)
        await session.rollback()
        raise e
    
async def update_archive(*,session: AsyncSession, archive: archive_schema.Archive) -> Archive:
    db_archive = await session.get(Archive, archive.id)
    
    if not db_archive:
        return None
    else:
        update_dict = archive.model_dump(exclude_unset=True)
        db_archive.sqlmodel_update(update_dict)
        db_archive.update_date = datetime.now()
        session.add(db_archive)
        await session.commit()
        await session.refresh(db_archive)
    return db_archive
    
async def create_file(*,session: AsyncSession, file: archive_schema.FileUpload,user_id:uuid.UUID) -> UserFiles:
    db_obj = UserFiles.model_validate(file,update={"user_id":user_id})
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

