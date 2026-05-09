"""
app/core/config/settings.py
"""

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    APP_NAME: str = "Career Copilot"

    MISTRAL_MODEL: str = "mistral"

    class Config:
        env_file = ".env"


settings = AppSettings()