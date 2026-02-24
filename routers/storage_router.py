import os

from fastapi import APIRouter, Query, HTTPException

from config import Config

storage_router = APIRouter(prefix="/storage", tags=["storage"])

@storage_router.get('/list')
def list_dir(path: str = Query("", description="Относительный путь в хранилище")):
    abs_path = os.path.abspath(os.path.join(Config.STORAGE_PATH, path))

    # защита от выхода за пределы STORAGE_PATH
    if not abs_path.startswith(os.path.abspath(Config.STORAGE_PATH)):
        raise HTTPException(status_code=400, detail="Invalid path")

    if not os.path.exists(abs_path):
        raise HTTPException(status_code=404, detail="Path not found")

    items = []
    for f in os.listdir(abs_path):
        full = os.path.join(abs_path, f)
        items.append({
            "name": f,
            "is_dir": os.path.isdir(full)
        })

    # Сортировка (сначала папки, потом файлы)
    items = sorted(items, key=lambda x: (not x['is_dir'], x['name'].lower()))

    return {"path": path, "items": items}