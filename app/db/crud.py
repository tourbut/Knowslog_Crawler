from app.models import *
from app.db.schemas import users as user_schema
from sqlmodel import Session, select
from app.utils.security import get_password_hash

def create_user(*, session: Session, user_create: user_schema.UserCreate) -> User:
    db_obj = User.model_validate(user_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def create_user_detail(*, session: Session, user_detail_create: user_schema.UserDetailCreate) -> UserDetail:
    db_obj = UserDetail.model_validate(user_detail_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def create_archive(*, session: Session, archive_create: user_schema.ArchiveCreate) -> Archive:
    db_obj = Archive.model_validate(archive_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj