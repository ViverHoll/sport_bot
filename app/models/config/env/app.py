from pydantic import BaseModel

from .postgres import PostgresConfig
from .redis import RedisConfig
from .telegram import TelegramConfig


class AppConfig(BaseModel):
    common: TelegramConfig
    postgres: PostgresConfig
    redis: RedisConfig
