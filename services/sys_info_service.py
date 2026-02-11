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
        raw_out = await self.cmd_runner_service.run(['sensors'])

        raw_out = raw_out.splitlines()
        chipset = raw_out[7]
        cpu = raw_out[8]
        vrm = raw_out[11]
        gpu = raw_out[23]
        gpu = 'GPU:  ' + gpu[6:-32]

        temperatures = {'chipset': chipset, 'cpu': cpu, 'vrm': vrm, 'gpu': gpu}

        return temperatures