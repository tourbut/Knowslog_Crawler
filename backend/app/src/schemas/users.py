from app.models import *
from sqlmodel import SQLModel
import uuid

class UserCreate(SQLModel):
    email: EmailStr | None = Field(default=None, max_length=255)
    username: str
    password: str
    name: str 
    age: int 
    discord_yn : bool 
    email_yn : bool 
    interests: str

class UserDetail(SQLModel):
    name: str 
    age: int 
    discord_yn : bool 
    email_yn : bool 
    interests: str

class UserPublic(SQLModel):
    id: uuid.UUID 
    username:str
    is_active: bool
    
class Token(SQLModel):
    username: str
    is_admin: bool = False
    access_token: str
    token_type: str = "bearer"

class TokenPayload(SQLModel):
    sub: uuid.UUID | None = None
