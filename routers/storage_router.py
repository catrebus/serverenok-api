from fastapi import APIRouter, Query, Depends

from core.dependencies import get_storage_service
from services import StorageServiceProtocol

storage_router = APIRouter(prefix="/storage", tags=["storage"])

@storage_router.get('/list')
async def list_dir(path: str = Query("", description="Относительный путь в хранилище"), storage: StorageServiceProtocol = Depends(get_storage_service)):
    return await storage.list_dir(path)