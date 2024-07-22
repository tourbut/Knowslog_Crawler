from app.models import *
from app.src.schemas import crawler as crawler_schema
from sqlmodel import Session, select
from app.src.utils.security import get_password_hash

async def create_archive(*,session: Session, archive: crawler_schema.Archive,user_id:int) -> Archive:
    db_obj = Archive.model_validate(archive,update={"user_id":user_id})
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj
