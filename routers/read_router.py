from fastapi import APIRouter, Depends

from core import container

read_router = APIRouter(prefix="/read", tags=["read"])

@read_router.get('/temperature')
async def get_temperature():
    info_service = container.info_service
    return await info_service.get_temperature()