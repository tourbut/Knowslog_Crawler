from app.models import *
from sqlmodel import SQLModel
from sqlmodel import Session, select

class UserCreate(SQLModel):
    email: EmailStr | None = Field(default=None, max_length=255)
    username: str
    password: str

class UserDetail(SQLModel):
    name: str 
    age: int 
    discord_yn : bool 
    email_yn : bool 
    llm_model: str 
    api_key: str
    interests: str

class UserPublic(SQLModel):
    id: int
    
class Token(SQLModel):
    username: str
    access_token: str
    token_type: str = "bearer"

class TokenPayload(SQLModel):
    sub: int | None = None
