from pydantic import BaseSettings
import os
from typing import Optional
from pathlib import Path
# env_location = Path("./.env").resolve()
env_location = Path("./.env").resolve()

class Settings(BaseSettings):
    DB_CONNECTION: Optional[str]
    DB_HOST: Optional[str]
    DB_PORT: Optional[str]
    DB_DATABASE: Optional[str]
    DB_USER: Optional[str]
    DB_PASSWORD: Optional[str]

    class Config:
        case_sensitive = True
        env_file = env_location
        env_file_encoding = "utf-8"

# Optional[str]