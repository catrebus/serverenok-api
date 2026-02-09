import os


class Config:
    SERVERENOK_API_HOST=os.getenv('SERVERENOK_API_HOST', '127.0.0.1')
    SERVERENOK_API_PORT=int(os.getenv('SERVERENOK_API_PORT', 8000))
    SERVERENOK_API_KEY=os.getenv('SERVERENOK_API_KEY', 'qweqwe')