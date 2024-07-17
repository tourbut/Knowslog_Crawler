from collections.abc import Generator, AsyncGenerator
from typing import Annotated

from sqlmodel import Session,create_engine


from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from fastapi import Depends

from config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
async_engine = create_async_engine(str(settings.SQLALCHEMY_DATABASE_URI))

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(async_engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]

SessionDep_async = Annotated[AsyncSession, Depends(get_async_db)]

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
