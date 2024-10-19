from pathlib import Path

from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings as _BaseSettings
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / "config.env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


class CommonConfig(BaseSettings, env_prefix="COMMON_"):
    bot_token: SecretStr
    support_url: str
    gpt_token: SecretStr
    proxy: str


class ChannelConfig(BaseSettings, env_prefix="CHANNEL_"):
    id: SecretStr
    url: str


class PostgresConfig(BaseSettings, env_prefix="POSTGRES_"):
    port: int
    host: str
    password: SecretStr
    username: str
    db_name: str
    data: str

    def build_url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            database=self.db_name,
            port=self.port,
            host=self.host,
            password=self.password.get_secret_value(),
            username=self.username
        )


class RedisConfig(BaseSettings, env_prefix="REDIS_"):
    port: int
    host: str
    db: int
    data: str

class AppConfig(BaseModel):
    common: CommonConfig
    channel: ChannelConfig
    postgres: PostgresConfig
    redis: RedisConfig
