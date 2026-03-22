import asyncio
import os
from abc import ABC, abstractmethod


class FoldersHelperProtocol(ABC):

    @abstractmethod
    async def get_folder_size(self, path: str) -> int: ...

class FoldersHelper(FoldersHelperProtocol):

    async def get_folder_size(self, path: str) -> int:
        """
        Асинхронно вычисляет суммарный размер всех файлов в папке
        """

        def calc_size():
            total = 0
            for root, dirs, files in os.walk(path):
                for f in files:
                    full_path = os.path.join(root, f)
                    try:
                        total += os.path.getsize(full_path)
                    except OSError: # Файл удалился во время подсчета
                        pass
            return total

        return await asyncio.to_thread(calc_size)