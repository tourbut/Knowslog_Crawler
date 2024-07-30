from app.models import *
from sqlmodel import SQLModel
from sqlmodel import Session, select

class Setting_LLM(SQLModel):
    source: str
    type: str
    name: str
    description: str
    input_price: float
    output_price: float
