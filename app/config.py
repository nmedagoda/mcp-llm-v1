import os

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379

settings = Settings()