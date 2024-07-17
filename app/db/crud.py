from models import *
from db.schemas import UserCreate, ArchiveCreate
from sqlmodel import Session, select
from utils.security import get_password_hash

def create_user(*, session: Session, user_create: UserCreate) -> User:
    db_obj = User.model_validate(user_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def create_archive(*, session: Session, archive_create: ArchiveCreate) -> Archive:
    db_obj = Archive.model_validate(archive_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj
