import uuid
from sqlmodel import SQLModel
from datetime import datetime

class SendMessage(SQLModel):
    chat_id: str
    user_llm_id: int 
    input: str
    
class Usage(SQLModel):
    user_llm_id: int 
    input_token:int 
    output_token:int

class OutMessage(SQLModel):
    content: str
    input_token: int | None = None
    output_token: int | None = None
    is_done: bool = False
    
class GetUserLLM(SQLModel):
    id: int
    source: str
    name: str
    api_key: str
    
class CreateChat(SQLModel):
    title: str
    user_llm_id: int

class ResponseChat(SQLModel):
    id: str
    
class GetChat(SQLModel):
    category: str = "chat"
    id: uuid.UUID
    title: str
    user_llm_id: int

class GetMessages(SQLModel):
    chat_id: str

class ReponseMessages(SQLModel):
    chat_id: uuid.UUID
    id: uuid.UUID
    name:str
    content: str
    is_user: bool
    create_date: datetime

class CreateMessage(SQLModel):
    chat_id: uuid.UUID 
    user_id: int
    name: str 
    content: str
    is_user: bool
    