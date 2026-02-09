from config import Config
from services.request_auth_service import APIKeyAuthService


class Container:
    def __init__(self):
        self.auth_service = APIKeyAuthService(Config.SERVERENOK_API_KEY)

container = Container()