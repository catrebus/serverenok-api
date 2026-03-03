import os
from abc import ABC, abstractmethod
from typing import List, Dict

from fastapi import HTTPException
from starlette.concurrency import run_in_threadpool


class StorageServiceProtocol(ABC):

    # Получение содержимого папки
    @abstractmethod
    def _sync_list_dir(self, rel_path: str) -> Dict[str, List[str]]: ...

    @abstractmethod
    async def list_dir(self, rel_path: str) -> Dict[str, List[str]]: ...

    # Отправка файла
    @abstractmethod
    def _sync_upload_file(self, src_path: str, dest_path: str) -> None: ...

    @abstractmethod
    async def upload_file(self, src_path: str, dest_path: str) -> None: ...

    # Скачивание файла
    @abstractmethod
    def _sync_download_file(self, src_path: str, dest_path: str) -> None: ...

    @abstractmethod
    async def download_file(self, src_path: str, dest_path: str) -> None: ...

    # Переименование файла
    @abstractmethod
    def _sync_rename_file(self, old_rel_path: str, new_rel_path: str) -> None: ...

    @abstractmethod
    async def rename_file(self, old_rel_path: str, new_rel_path: str) -> None: ...


class StorageService(StorageServiceProtocol):
    def __init__(self, base_path: str):
        self.base_path = base_path #/api_storage

    # Получение содержимого папки
    def _sync_list_dir(self, rel_path: str) -> Dict[str, List[str]]:
        abs_path = os.path.abspath(os.path.join(self.base_path, rel_path))

        # защита от выхода за пределы STORAGE_PATH
        if not abs_path.startswith(os.path.abspath(self.base_path)):
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

        return {"path": rel_path, "items": items}

    async def list_dir(self, rel_path: str) -> Dict[str, List[str]]:
        return await run_in_threadpool(self._sync_list_dir, rel_path)

    # Отправка файла
    def _sync_upload_file(self, src_path: str, dest_path: str) -> None: ...

    async def upload_file(self, src_path: str, dest_path: str) -> None: ...

    # Скачивание файла
    def _sync_download_file(self, src_path: str, dest_path: str) -> None: ...

    async def download_file(self, src_path: str, dest_path: str) -> None: ...

    # Переименование файла
    def _sync_rename_file(self, old_rel_path: str, new_rel_path: str) -> None: ...

    async def rename_file(self, old_rel_path: str, new_rel_path: str) -> None: ...