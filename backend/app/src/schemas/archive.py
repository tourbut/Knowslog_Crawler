from sqlmodel import SQLModel

class ArchiveURL(SQLModel):
    url: str
    html: str
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

class Refine(SQLModel):
    user_id: int 
    title: str 
    author: str
    content: str 

class Usage(SQLModel):
    user_llm_id: int 
    input_token:int 
    output_token:int
    
class ResponseArchive(SQLModel):
    id: int
    category: str
    language: str
    title: str 
    author: str 
    content: str
    refine_content: str| None
    input_token: int| None
    output_token: int | None
    url : str 
    dom : str

class ArchiveList(SQLModel):
    id: int
    category: str
    title: str
    url:str
    
class GetUserLLM(SQLModel):
    id: int
    source: str
    name: str
    api_key: str