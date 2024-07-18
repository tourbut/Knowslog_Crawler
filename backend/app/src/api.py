from fastapi import APIRouter
from app.src.routes import users,crawler

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(crawler.router, prefix="/crawler", tags=["crawler"])