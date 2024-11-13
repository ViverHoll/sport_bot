# from typing import Callable, Any, Awaitable, TYPE_CHECKING
#
# from aiogram import BaseMiddleware
# from aiogram.types import TelegramObject
#
# if TYPE_CHECKING:
#     from app.services.db import Database
#
#
# class AdminMiddleware(BaseMiddleware):
#     async def __call__(
#             self,
#             handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
#             event: TelegramObject,
#             data: dict[str, Any],
#     ) -> Any:
#         db: Database = data["db"]
#
#
#
#
#