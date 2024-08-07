from app.models import *
from sqlmodel import SQLModel

class Get_LLM(SQLModel):
    id:int
    source: str
    type: str
    name: str
    description: str
    input_price: float
    output_price: float

class Create_Apikey(SQLModel):
    api_name:str
    api_key:str 
    active_yn:bool 
    
class Get_Apikey(SQLModel):
    id:int
    api_name:str
    api_key:str 
    active_yn:bool 
    
class Get_UserLLM(SQLModel):
    id:int
    source:str
    name:str
    api_key:str
    active_yn:bool

class Create_UserLLM(SQLModel):
    llm_id:int
    api_id:int
    active_yn:bool

class Update_UserLLM(SQLModel):
    id:int
    llm_id:int
    api_id:int
    active_yn:bool

class Delete_UserLLM(SQLModel):
    id:int