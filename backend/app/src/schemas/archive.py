from app.models import *
from sqlmodel import SQLModel

class ArchiveURL(SQLModel):
    url: str
    auto_translate: bool
    auto_summarize: bool

class Archive(SQLModel):
    category: str
    language: str
    title: str 
    author: str 
    content: str 
    url : str 
    dom : str