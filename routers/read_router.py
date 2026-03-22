from fastapi import APIRouter, Depends


from core.dependencies import get_info_service
from services import SysInfoServiceProtocol

read_router = APIRouter(prefix="/read", tags=["read"])

@read_router.get('/temperature')
async def get_temperature(
        info_service: SysInfoServiceProtocol = Depends(get_info_service)
):
    return await info_service.get_temperature()