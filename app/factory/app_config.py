from app.app_config import (
    AppConfig,
    ChannelConfig,
    CommonConfig,
    PostgresConfig,
    RedisConfig
)


def create_app_config() -> AppConfig:
    return AppConfig(
        common=CommonConfig(),
        channel=ChannelConfig(),
        postgres=PostgresConfig(),
        redis=RedisConfig()
    )
