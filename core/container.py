from config import Config
from services import APIKeyAuthService, SysInfoService, StorageService
from utils import CmdRunner, Parser, FoldersHelper


class Container:
    def __init__(self):
        self.config = Config()

        self._cmd_runner = None
        self._parser = None
        self._auth_service = None
        self._info_service = None
        self._storage_service = None
        self._folders_helper = None

    # ---------- Infra ----------

    @property
    def cmd_runner(self):
        if self._cmd_runner is None:
            self._cmd_runner = CmdRunner()
        return self._cmd_runner

    @property
    def parser(self):
        if self._parser is None:
            self._parser = Parser()
        return self._parser

    @property
    def folders_helper(self):
        if self._folders_helper is None:
            self._folders_helper = FoldersHelper()
        return self._folders_helper

    # ---------- Services ----------

    @property
    def auth_service(self):
        if self._auth_service is None:
            self._auth_service = APIKeyAuthService(
                self.config.SERVERENOK_API_KEY
            )
        return self._auth_service

    @property
    def info_service(self):
        if self._info_service is None:
            self._info_service = SysInfoService(
                self.cmd_runner,
                self.parser
            )
        return self._info_service

    @property
    def storage_service(self):
        if self._storage_service is None:
            self._storage_service = StorageService(
                self.config.STORAGE_PATH
            )
        return self._storage_service


container = Container()