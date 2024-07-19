from app.models import *
from sqlmodel import SQLModel
from sqlmodel import Session, select

class UserCreate(SQLModel):
    email: EmailStr | None = Field(default=None, max_length=255)
    username: str
    password: str

class UserPublic(SQLModel):
    id: int
    
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(SQLModel):
    sub: int | None = None
