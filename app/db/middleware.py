from collections.abc import Awaitable, Callable
from typing import Any, TYPE_CHECKING

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from .dao.holder import HolderDAO

if TYPE_CHECKING:
    from .session import SessionPool


class DatabaseMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any],
    ) -> Any:
        session_pool: SessionPool = data["session_pool"]

        async with session_pool() as session:
            data["db"] = HolderDAO(session=session)
            return await handler(event, data)
