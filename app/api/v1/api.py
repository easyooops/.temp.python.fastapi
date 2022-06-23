from fastapi import APIRouter
from app.api.v1.endpoints import item, user

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(item.router, tags=["items"])