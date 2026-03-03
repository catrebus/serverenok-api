from fastapi import APIRouter, Query

from core import container

storage_router = APIRouter(prefix="/storage", tags=["storage"])

@storage_router.get('/list')
async def list_dir(path: str = Query("", description="Относительный путь в хранилище")):
    storage = container.storage_service
    return await storage.list_dir(path)