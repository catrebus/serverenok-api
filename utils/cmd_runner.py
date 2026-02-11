import asyncio
from abc import ABC, abstractmethod
from typing import List


class CmdRunnerProtocol(ABC):

    @abstractmethod
    async def run(self, cmd:List[str]) -> str: ...

class CmdRunner(CmdRunnerProtocol):

    async def run(self, cmd:List[str], timeout: int = 5) -> str:
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        try:
            stdout, stderr = await asyncio.wait_for(
                proc.communicate(),
                timeout=timeout
            )
        except asyncio.TimeoutError:
            proc.kill()
            await proc.wait()
            return "Command timeout"

        if proc.returncode != 0:
            return stderr.decode()

        return stdout.decode()