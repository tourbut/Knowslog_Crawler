from typing import List
from app.models import *
from app.src.schemas import admin as admin_schema
from sqlmodel import Session, select


async def create_llm(*, session: Session, llm_create: admin_schema.LLMCreate) -> LLM:
    db_obj = LLM.model_validate(llm_create)
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

async def get_llm_settings(*, session: Session) -> List[LLM]| None:
    statement = select(LLM)
    llm = await session.exec(statement)

    if not llm:
        return None
    else:
        return llm.all()