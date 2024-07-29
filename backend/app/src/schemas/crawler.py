from app.models import *
from sqlmodel import SQLModel
from sqlmodel import Session, select

class ArchiveURL(SQLModel):
    url: str

class Archive(SQLModel):
    category: str
    language: str
    title: str 
    author: str 
    content: str 
    url : str 
    dom : str