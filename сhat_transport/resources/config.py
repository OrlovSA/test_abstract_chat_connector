import sys

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

from сhat_transport.resources.enum import ChatTransportEnum


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    CHAT_TRANSPORT: ChatTransportEnum
    TELEGRAM_API_TOKEN: str
    TELEGRAM_CHAT_ID: int


settings = Settings()

logger.add(
    sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO"
)
