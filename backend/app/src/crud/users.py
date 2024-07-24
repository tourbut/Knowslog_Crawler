from app.models import *
from app.src.schemas import users as user_schema
from sqlmodel import Session, select
from app.src.utils.security import get_password_hash, verify_password


async def get_user_by_email(*, session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    session_user = await session.exec(statement)
    return session_user.first()

async def authenticate(*, session: Session, email: str, password: str) -> User | None:
    db_user = await get_user_by_email(session=session, email=email)
    if not db_user:
        return None
    if not await verify_password(password, db_user.password):
        return None
    return db_user

async def acreate_user(*, session: Session, user_create: user_schema.UserCreate) -> User:
    
    db_obj = User.model_validate(
        user_create, update={"password": await get_password_hash(user_create.password)})
    
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj


async def get_detail(*, session: Session, user_id: int) -> UserDetail | None:
    statement = select(UserDetail).where(UserDetail.user_id == user_id)
    session_user = await session.exec(statement)
    return session_user.first()

async def create_detail(*, session: Session, user_detail: user_schema.UserDetail, user_id: int) -> UserDetail:
    
    db_obj = UserDetail.model_validate(user_detail, update={"user_id": user_id})
    
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

async def update_detail(*, session: Session, user_detail: user_schema.UserDetail, user_id: int) -> UserDetail:
    db_obj = UserDetail.model_validate(user_detail, update={"user_id": user_id})
    detail = await get_detail(session=session, user_id=user_id)
    
    if not detail:
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
    else:
        detail.name = db_obj.name
        detail.age = db_obj.age
        detail.discord_yn = db_obj.discord_yn
        detail.email_yn = db_obj.email_yn
        detail.llm_model = db_obj.llm_model
        detail.api_key = db_obj.api_key
        detail.interests = db_obj.interests
        detail.update_date = datetime.now()

        await session.commit()
    
    return db_obj