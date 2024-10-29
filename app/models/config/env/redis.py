from .base import EnvSettings


class RedisConfig(EnvSettings, env_prefix="REDIS_"):
    port: int
    host: str
    db: int
    data: str
