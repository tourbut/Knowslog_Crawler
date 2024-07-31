from typing import Any, Annotated, List
from datetime import timedelta

from fastapi import APIRouter, HTTPException

from app.src.deps import SessionDep_async,CurrentUser
from app.src.crud import admin as admin_crud
from app.src.schemas import admin as admin_schema

from app.core.config import settings

router = APIRouter()

@router.get("/get_llm_settings", response_model=List[admin_schema.LLMSelect])
async def get_llm_settings(*, session: SessionDep_async, current_user: CurrentUser) -> Any:
    """
    Get LLM Settings
    """
    
    if not current_user.is_admin:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    
    settings = await admin_crud.get_llm_settings(session=session)
    return settings

@router.post("/create_llm", response_model=admin_schema.LLMSelect)
async def create_llm(*, session: SessionDep_async, current_user: CurrentUser, llm_create: admin_schema.LLMCreate) -> Any:
    """
    Create LLM
    """
    
    if not current_user.is_admin:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    
    llm = await admin_crud.create_llm(session=session, llm_create=llm_create)
    return llm
