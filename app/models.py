from sqlmodel import Field, Relationship, SQLModel,DateTime,String,Integer,JSON
from pydantic import EmailStr

from datetime import datetime

from sympy import content

class CommonBase(SQLModel):
    create_date: datetime = Field(default=datetime.now())
    update_date: datetime = Field(default=datetime.now())
    delete_yn: bool = Field(default=False)

class User(CommonBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, nullable=False)
    password: str = Field(nullable=False)
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    
class UserDetail(CommonBase, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    age: int = Field(nullable=False)
    discord_yn : bool = Field(default=False)
    email_yn : bool = Field(default=False)
    llm_model: str | None = Field(nullable=True)
    api_key: str | None = Field(nullable=True)
    interests: str | None = Field(nullable=True)
    json_data: JSON | None = Field(nullable=True)
    
class Archive(CommonBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    category: str = Field(nullable=False)
    collect_ymd: str = Field(nullable=False)
    language: str = Field(nullable=False)
    title: str | None = Field(nullable=True)
    author: str | None = Field(nullable=True)
    content: str = Field(nullable=False)
    url : str = Field(nullable=False)

class Refine(CommonBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    archive_id: int = Field(foreign_key="archive.id")
    refine_ymd: str = Field(nullable=False)
    title: str | None = Field(nullable=True)
    author: str | None = Field(nullable=True)
    content: str = Field(nullable=False)
    