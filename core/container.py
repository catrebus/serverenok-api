from config import Config
from services import APIKeyAuthService, SysInfoService
from utils import CmdRunner, Parser


class Container:
    def __init__(self):
        # ------ Config ------
        self.config = Config()

        # ------ Singletons ------
        self.auth_service = APIKeyAuthService(Config.SERVERENOK_API_KEY)
        self.cmd_runner = CmdRunner()
        self.parser = Parser()
        self.infoService = SysInfoService(self.cmd_runner, self.parser)

    def get_info_service(self):
        return self.infoService


container = Container()