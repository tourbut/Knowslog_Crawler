from typing import List
from app.models import *
from app.src.schemas import settings as settings_schema
from sqlmodel import Session, select

async def get_llm_settings(*, session: Session) -> List[LLM]| None:
    statement = select(LLM)
    llm = await session.exec(statement)

    if not llm:
        return None
    else:
        return llm.all()