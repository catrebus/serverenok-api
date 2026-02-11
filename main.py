import uvicorn
from fastapi import FastAPI

from config import Config
from core import container
from middlewares import AuthMiddleware
from routers import main_router

app = FastAPI()

# Подключение router
app.include_router(main_router)

# Подключение middlewares
app.add_middleware(AuthMiddleware, auth_service=container.auth_service)

if __name__ == "__main__":
    uvicorn.run(app, host=Config.SERVERENOK_API_HOST, port=Config.SERVERENOK_API_PORT)