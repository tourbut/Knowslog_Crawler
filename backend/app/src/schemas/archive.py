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
    work_cd: str
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
    translate_content: str| None
    translate_input_token: int| None
    translate_output_token: int | None
    summarize_content: str| None
    summarize_input_token: int| None
    summarize_output_token: int | None
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
    
class Update_Archive(SQLModel):
    id: int
    category: str|None = None
    language: str|None = None
    title: str|None = None
    author: str|None = None
    content: str|None = None
    url : str|None = None
    dom : str|None = None
    delete_yn: bool|None = None