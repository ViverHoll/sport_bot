from sqlalchemy import URL
from pydantic import SecretStr

from .base import EnvSettings


class PostgresConfig(EnvSettings, env_prefix="POSTGRES_"):
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
            username=self.username,
        )
