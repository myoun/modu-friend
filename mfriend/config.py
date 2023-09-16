from pydantic import BaseSettings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
ENV_FILE = os.path.join(BASE_DIR, ".env")

class Settings(BaseSettings):
    OPENAI_TOKEN: str = 'UNDEFINED'
    DB_URL: str = 'UNDEFINED'

    class Config:
        env_file = ENV_FILE