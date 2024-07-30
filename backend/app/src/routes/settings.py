from typing import Any, Annotated, List
from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends
from psycopg import DatabaseError

from app.src.utils import security
from fastapi.security import OAuth2PasswordRequestForm

from app.src.deps import SessionDep_async,CurrentUser
from app.src.crud import settings as settings_crud
from app.src.schemas import settings as settings_schema

from app.core.config import settings

router = APIRouter()

@router.get("/get_llm_settings", response_model=List[settings_schema.Setting_LLM])
async def get_llm_settings(*, session: SessionDep_async, current_user: CurrentUser) -> Any:
    """
    Get LLM Settings
    """
    settings = await settings_crud.get_llm_settings(session=session)
    return settings