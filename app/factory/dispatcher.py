from aiogram import Dispatcher
from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage
from aiogram_dialog import setup_dialogs

from app.models.config import AppConfig
from app.services.db import DatabaseMiddleware
from app.services.db.session import create_session_pool
from app.services.dialogs import setup_all_dialogs
from app.telegram.handlers import handler_router
from app.telegram.middleware.outer import CheckUserMiddleware
from app.telegram.state import state_router

from .gpt import GptClient
from .redis import create_redis
from .cache import create_ttl_cache


def _setup_outer_middleware(dp: Dispatcher) -> None:
    dp.update.middleware(DatabaseMiddleware())
    dp.update.middleware(CheckUserMiddleware())


async def create_dispatcher(config: AppConfig) -> Dispatcher:
    """Create dispatcher with routers, middlewares."""
    dp = Dispatcher(
        config=config,
        gpt=GptClient(config),
        storage=RedisStorage(
            redis=await create_redis(config),
            key_builder=DefaultKeyBuilder(
                with_destiny=True,
            ),
        ),
        session_pool=create_session_pool(
            url=config.postgres.build_url(),
        ),
        ttl_cache=create_ttl_cache(
            max_size=100_000,
            ttl=60,
        ),
    )

    _setup_outer_middleware(dp)

    dp.include_routers(
        handler_router,
        state_router,
        setup_all_dialogs(),
        # handler_router,
    )

    setup_dialogs(dp)

    return dp
