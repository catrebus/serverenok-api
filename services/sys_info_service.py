from abc import ABC, abstractmethod

from utils import CmdRunnerProtocol, ParserProtocol


class SysInfoServiceProtocol(ABC):

    @abstractmethod
    async def get_temperature(self): ...

class SysInfoService(SysInfoServiceProtocol):
    def __init__(self, cmd_runner_service: CmdRunnerProtocol, parser: ParserProtocol):
        self.cmd_runner_service = cmd_runner_service
        self.parser = parser

    # Температуры комплектующих
    async def get_temperature(self):
        raw_out = await self.cmd_runner_service.run(['sensors'])
        parsed_out = await self.parser.parse_sensors_json(raw_out)

        return parsed_out