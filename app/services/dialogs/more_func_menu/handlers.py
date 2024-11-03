from typing import Any, TYPE_CHECKING

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

from app.services.dialogs.states import MoreFuncStates

if TYPE_CHECKING:
    from aiogram import Bot

    from app.app_config import AppConfig


async def get_feedback_user(
        message: Message,
        _: ManagedTextInput,
        manager: DialogManager,
        text: str,
) -> None:
    bot: Bot = manager.middleware_data["bot"]
    config: AppConfig = manager.middleware_data["config"]

    for admin in config.common.admins:
        await bot.send_message(
            chat_id=admin,
            text=f"Пришел отзыв о боте!\n"
                 f"@{message.from_user.username} ({message.from_user.id})\n\n"
                 f"{text}",
        )
    await message.answer(
        "Ваше сообщение успешно принято.\n"
        "Ожидайте обратной связи от админа",
    )
    await manager.switch_to(MoreFuncStates.menu)


async def get_idea_user(
        message: Message,
        _: ManagedTextInput,
        manager: DialogManager,
        text: str,
) -> None:
    bot: Bot = manager.middleware_data["bot"]
    config: AppConfig = manager.middleware_data["config"]

    for admin in config.common.admins:
        await bot.send_message(
            chat_id=admin,
            text=f"Пришла идея для бота!\n"
                 f"@{message.from_user.username}({message.from_user.id})\n\n"
                 f"{text}",
        )
    await message.answer(
        "Ваша идея успешно принята.\n"
        "Ожидайте обратной связи от админа",
    )
    await manager.switch_to(MoreFuncStates.menu)


async def coming_soon(
        callback: CallbackQuery,
        *_args: Any,
) -> None:
    await callback.answer(
        "В разработке... 🛠",
        show_alert=True,
    )
