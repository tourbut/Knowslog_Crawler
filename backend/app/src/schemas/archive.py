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

class ResponseArchive(SQLModel):
    id: int
    category: str
    language: str
    title: str 
    author: str 
    content: str 
    url : str 
    dom : str

class ArchiveList(SQLModel):
    id: int
    category: str
    title: str
    url:str