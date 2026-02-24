from fastapi import APIRouter

from .read_router import read_router
from .admin_router import admin_router
from .storage_router import storage_router

main_router = APIRouter()
main_router.include_router(read_router)
main_router.include_router(admin_router)
main_router.include_router(storage_router)