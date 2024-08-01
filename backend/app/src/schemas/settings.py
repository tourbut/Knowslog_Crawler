from app.models import *
from sqlmodel import SQLModel

class Get_LLM(SQLModel):
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
    source:int
    name:int
    api_key:int
    active_yn:bool

class Create_UserLLM(SQLModel):
    llm_id:int
    api_id:int
    active_yn:bool
    