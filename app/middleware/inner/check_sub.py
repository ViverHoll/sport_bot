from typing import Any, Awaitable, Callable, TYPE_CHECKING

from aiogram import BaseMiddleware, Bot
from aiogram.types import CallbackQuery, Message

if TYPE_CHECKING:
    from app.app_config import AppConfig
from app.keyboards.user.inline import get_sub_menu


class CheckSubMessageMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:
        bot: Bot = data["bot"]
        config: AppConfig = data["config"]

        status_user = await bot.get_chat_member(
            chat_id=config.channel.id.get_secret_value(),
            user_id=event.from_user.id
        )

        if status_user.status == "left":
            return await event.answer("Необходимо подписаться на канал",
                                      reply_markup=get_sub_menu(config.channel.url))
        return await handler(event, data)


class CheckSubCallbackMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[CallbackQuery, dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: dict[str, Any]
    ) -> Any:
        bot: Bot = data["bot"]
        config: AppConfig = data["config"]

        status_user = await bot.get_chat_member(
            chat_id=config.channel.id.get_secret_value(),
            user_id=event.from_user.id
        )

        if status_user.status == "left":
            return await event.message.answer("Необходимо подписаться на канал",
                                              reply_markup=get_sub_menu(config.channel.url))
        return await handler(event, data)


"""49"""
