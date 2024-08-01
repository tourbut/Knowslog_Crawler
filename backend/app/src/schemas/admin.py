from app.models import *
from sqlmodel import SQLModel

class LLMCreate(SQLModel):
    source: str
    type: str
    name: str
    description: str
    input_price: float
    output_price: float
    is_active: bool

class Get_LLM(SQLModel):
    id: int
    source: str
    type: str
    name: str
    description: str
    input_price: float
    output_price: float
    is_active: bool
