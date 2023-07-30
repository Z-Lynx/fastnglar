# app/config/settings.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "My FastAPI Application"
    APP_DESCRIPTION: str = "A simple FastAPI application"
    APP_VERSION: str = "1.0.0"
    MYSQL_DATABASE_HOST: str = "localhost"
    MYSQL_DATABASE_PORT: int = 3306
    MYSQL_DATABASE_USER: str = "root"
    MYSQL_DATABASE_PASSWORD: str = "root123"
    MYSQL_DATABASE_NAME: str = "quanlydatsanbong"

    class Config:
        env_file = ".env"

settings = Settings()