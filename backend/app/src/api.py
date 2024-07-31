from fastapi import APIRouter
from app.src.routes import users,crawler,settings,admin

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(crawler.router, prefix="/crawler", tags=["crawler"])
api_router.include_router(settings.router, prefix="/settings", tags=["settings"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])