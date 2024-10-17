from sqlmodel import SQLModel
import uuid
from typing import List

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
    user_id: uuid.UUID  
    work_cd: str
    content: str 

class Usage(SQLModel):
    user_llm_id: uuid.UUID  
    input_token:int 
    output_token:int
    
class ResponseArchive(SQLModel):
    id: uuid.UUID 
    category: str =''
    language: str =''
    title: str =''
    author: str =''
    content: str =''
    translate_content: str| None = None
    translate_input_token: int| None = None
    translate_output_token: int | None = None
    summarize_content: str| None = None
    summarize_input_token: int| None = None
    summarize_output_token: int | None = None
    url : str =''
    dom : str =''

class ArchiveList(SQLModel):
    id: uuid.UUID 
    category: str
    title: str
    url:str
    

class GetUserLLM(SQLModel):
    id: uuid.UUID 
    source: str
    name: str
    api_key: str
    llm_id: uuid.UUID
    
class Update_Archive(SQLModel):
    id: uuid.UUID 
    category: str|None = None
    language: str|None = None
    title: str|None = None
    author: str|None = None
    content: str|None = None
    url : str|None = None
    dom : str|None = None
    delete_yn: bool|None = None

class DeleteFile(SQLModel):
    id: uuid.UUID

class FileUpload(SQLModel):
    file_name:str
    file_path:str
    file_size:int
    file_type:str
    file_ext:str
    file_desc:str | None = None
    embedding_yn:bool = False
    embedding_model_id:uuid.UUID | None = None
    collection_id:uuid.UUID | None = None
    
class ResponseFile(SQLModel):
    id: uuid.UUID
    file_name:str
    file_size:int
    file_ext:str
    file_desc:str | None = None
    contents:List[str] = []
    
class ResponseArchiveList(SQLModel):
    archive_list: List[ArchiveList]
    file_list: List[ResponseFile]
    