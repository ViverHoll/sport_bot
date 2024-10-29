import logging

from redis.asyncio import ConnectionPool, Redis

from app.models.config import AppConfig

logger = logging.getLogger(__name__)


async def create_redis(config: AppConfig) -> Redis:
    redis = Redis(
        connection_pool=ConnectionPool(
            host=config.redis.host,
            port=config.redis.port,
            db=config.redis.db
        )
    )

    info = await redis.info()
    logger.debug(info["redis_version"])
    response = await redis.ping()
    if response:
        logger.info("Подключение успешно!")
    else:
        logger.error("Не удалось подключиться к Redis.")
    return redis
