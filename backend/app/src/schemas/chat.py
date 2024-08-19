from sqlmodel import SQLModel

class SendMessage(SQLModel):
    input: str

class OutMessage(SQLModel):
    content: str
    input_token: int | None = None
    output_token: int | None = None
    
class GetUserLLM(SQLModel):
    id: int
    source: str
    name: str
    api_key: str