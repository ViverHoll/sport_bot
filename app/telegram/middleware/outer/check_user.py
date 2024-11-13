from typing import Any, Awaitable, Callable, TYPE_CHECKING

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, User

if TYPE_CHECKING:
    from app.services.db import HolderDAO

from app.models.dataclasses import UserType


class CheckUserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any],
    ) -> Any:
        """Проверка пользователя на существование в базе."""
        user: User = data["event_from_user"]
        db: HolderDAO = data["db"]
        bot: Bot = data["bot"]

        if not user:
            return await handler(event, data)

        user_ = await db.users.get_user(user_id=user.id)

        if not user_:
            await db.users.add_user(
                user_id=user.id,
                username=user.username,
            )
            user_ = await db.users.get_user(user_id=user.id)
            await bot.send_message(
                chat_id=789080569,
                text=f"Пользователь {user.username}({user.id}) добавлен в базу данных\n\n"
                     f"{user.full_name}",
            )

        data["user"] = UserType(**user_.__dict__)

        return await handler(event, data)
