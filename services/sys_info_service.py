from abc import ABC, abstractmethod

from utils import CmdRunnerProtocol


class SysInfoServiceProtocol(ABC):

    @abstractmethod
    async def get_temperature(self): ...

class SysInfoService(SysInfoServiceProtocol):
    def __init__(self, cmd_runner_service: CmdRunnerProtocol):
        self.cmd_runner_service = cmd_runner_service

    # Температуры комплектующих
    async def get_temperature(self):
        return await self.cmd_runner_service.run(['sensors'])