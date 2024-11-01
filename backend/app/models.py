from sqlmodel import Field, SQLModel, desc
from pydantic import EmailStr
import uuid
from datetime import datetime
from typing import Optional

class CommonBase(SQLModel):
    create_date: datetime = Field(default=datetime.now())
    update_date: datetime = Field(default=datetime.now())
    delete_yn: bool = Field(default=False)

class User(CommonBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    username: str = Field(unique=True, nullable=False, description="유저ID")
    password: str = Field(nullable=False, description="비밀번호")
    email: EmailStr = Field(unique=True, index=True, max_length=255,description="이메일")
    name: str = Field(nullable=False,description="이름")
    age: int = Field(nullable=False,description="나이")
    discord_yn : bool = Field(default=False,description="디스코드 수신여부")
    email_yn : bool = Field(default=False,description="이메일 수신여부")
    interests: str | None = Field(nullable=True,description="관심사")
    is_active: bool = Field(default=True,description="활성화여부")
    is_admin: bool = Field(default=False,description="관리자여부")

class LLM(CommonBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    source: str = Field(nullable=False)
    type: str = Field(nullable=False)
    name: str = Field(nullable=False)
    description: str | None = Field(nullable=True)
    input_price: float = Field(nullable=False)
    output_price: float = Field(nullable=False)
    is_active: bool = Field(default=True)

class UserAPIKey(CommonBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    user_id: uuid.UUID = Field(foreign_key="user.id")
    api_name:str = Field(nullable=False)
    api_key:str = Field(nullable=False)
    active_yn:bool = Field(default=True)

class UserLLM(CommonBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    user_id: uuid.UUID = Field(foreign_key="user.id")
    llm_id: uuid.UUID = Field(foreign_key="llm.id")
    api_id: uuid.UUID = Field(foreign_key="userapikey.id")
    active_yn:bool = Field(default=True)

class UserUsage(CommonBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    user_llm_id: uuid.UUID = Field(foreign_key="userllm.id")
    usage_date:datetime = Field(default=datetime.now())
    input_token:int = Field(nullable=False)
    output_token:int = Field(nullable=False)

class UserFiles(CommonBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    user_id: uuid.UUID = Field(foreign_key="user.id")
    file_name:str = Field(nullable=False,description="파일명")
    file_path:str = Field(nullable=False,description="파일경로")
    file_size:int = Field(nullable=False,description="파일크기")
    file_type:str = Field(nullable=False,description="파일타입")
    file_ext:str = Field(nullable=False,description="파일확장자")
    file_desc:str | None = Field(nullable=True,description="파일설명")
    embedding_yn:bool = Field(default=False,nullable=True,description="임베딩여부")
    embedding_model_id:Optional[uuid.UUID] = Field(foreign_key="llm.id",nullable=True,description="임베딩모델ID")
    collection_id:Optional[uuid.UUID] = Field(nullable=True,description="컬렉션ID")

class Archive(CommonBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    user_id: uuid.UUID = Field(foreign_key="user.id")
    category: str = Field(nullable=False)
    language: str = Field(nullable=False)
    title: str | None = Field(nullable=True)
    author: str | None = Field(nullable=True)
    content: str = Field(nullable=False)
    url : str = Field(nullable=False)
    dom: str | None = Field(nullable=True)
    embedding_yn:bool = Field(default=False,nullable=True,description="임베딩여부")
    embedding_model_id:Optional[uuid.UUID] = Field(foreign_key="llm.id",nullable=True,description="임베딩모델ID")
    collection_id:Optional[uuid.UUID] = Field(nullable=True,description="컬렉션ID")

class Refine(CommonBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    archive_id: uuid.UUID = Field(foreign_key="archive.id", nullable=False, description="아카이브ID")
    user_id: uuid.UUID = Field(foreign_key="user.id", nullable=False, description="유저ID")
    work_cd: str = Field(nullable=False, description="작업코드")
    content: str = Field(nullable=False, description="내용")
    
class UserPrompt(CommonBase,table=True):
    user_id: uuid.UUID = Field(foreign_key="user.id", primary_key=True)
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    instruct_prompt: str | None = Field(nullable=True)
    response_prompt: str | None = Field(nullable=True)

class SystemPrompt(CommonBase,table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    user_id: uuid.UUID = Field(foreign_key="user.id", description="유저ID")
    work_cd: str = Field(nullable=False, description="작업코드")
    description: str | None = Field(nullable=True, description="설명")
    instruct_prompt: str | None = Field(nullable=True, description="지시 프롬프트")
    response_prompt: str | None = Field(nullable=True, description="응답 프롬프트")

class ClsfCode(CommonBase,table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    clsf_cd: str = Field(nullable=False, description="분류코드")
    clsf_nm: str = Field(nullable=False, description="분류명")
    clsf_desc: str | None = Field(nullable=True, description="분류설명")

class CommonCode(CommonBase,table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    clsf_cd: str = Field(nullable=False, description="분류코드")
    code: str = Field(nullable=False, description="코드")
    code_nm: str = Field(nullable=False, description="코드명")
    code_desc: str | None = Field(nullable=True, description="코드설명")

class Chats(CommonBase,table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    user_id: uuid.UUID  = Field(foreign_key="user.id", description="유저ID")
    title: str = Field(nullable=False, description="채팅명")
    user_llm_id: uuid.UUID  = Field(foreign_key="userllm.id", description="유저LLMID")
    user_file_id: uuid.UUID  = Field(foreign_key="userfiles.id", description="유저파일ID")

class Messages(CommonBase,table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, description="ID")
    chat_id: uuid.UUID = Field(foreign_key="chats.id", description="채팅ID")
    user_id: uuid.UUID  = Field(foreign_key="user.id", description="유저ID")
    name:str = Field(nullable=False, description="이름")
    content: str = Field(nullable=False, description="내용")
    is_user: bool = Field(nullable=False, description="유저여부")


"""
class CrewAgent(CommonBase,table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    role: str = Field(nullable=False)
    goal: str = Field(nullable=False)
    backstory: str = Field(nullable=False)
    llm:str | None = Field(nullable=True,default="gpt-4o")
    tools:str | None = Field(nullable=True,default=None)
    function_calling_llm:str | None = Field(nullable=True)
    max_iter:int | None = Field(nullable=True,default=25)
    max_rpm:int | None = Field(nullable=True,default=None)
    max_execution_time:int | None = Field(nullable=True,default=None)
    verbose:bool | None = Field(nullable=True,default=False)
    allow_delegation:bool | None = Field(nullable=True,default=True)
    step_callback:str | None = Field(nullable=True,default=None)
    cache:bool | None = Field(nullable=True,default=True)
    system_template:str | None = Field(nullable=True,default=None)
    prompt_template:str | None = Field(nullable=True,default=None)
    response_template:str | None = Field(nullable=True,default=None)

class CrewTask(CommonBase,table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    agent_id: int = Field(foreign_key="crewagent.id", primary_key=True)
    id: int | None = Field(default=None, primary_key=True)
    description:str = Field(nullable=False)
    expected_output:str = Field(nullable=False)
    tools:str | None = Field(nullable=True)
    async_execution:bool | None = Field(nullable=True,default=False)
    context:str | None = Field(nullable=True)
    config:str | None = Field(nullable=True)
    output_json:str | None = Field(nullable=True)
    output_pydantic:str | None = Field(nullable=True)
    output_file:str | None = Field(nullable=True)
    output:str | None = Field(nullable=True)
    callback:str | None = Field(nullable=True)
    human_input:bool | None = Field(nullable=True,default=False)
"""