from app.models.config.env import (
    AppConfig,
    TelegramConfig,
    PostgresConfig,
    RedisConfig
)


def create_app_config() -> AppConfig:
    return AppConfig(
        common=TelegramConfig(),
        postgres=PostgresConfig(),
        redis=RedisConfig()
    )
