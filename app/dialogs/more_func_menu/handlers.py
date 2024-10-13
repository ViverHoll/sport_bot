from typing import Any

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from app.dialogs.states import MoreFuncStates


async def get_feedback_user(
        message: Message,
        _: MessageInput,
        manager: DialogManager
) -> None:
    await message.answer(
        "Ваше сообщение успешно принято.\n"
        "Ожидайте обратной связи от админа"
    )
    await manager.switch_to(MoreFuncStates.menu)


async def get_idea_user(
        message: Message,
        _: MessageInput,
        manager: DialogManager
) -> None:
    await message.answer(
        "Ваша идея успешно принята.\n"
        "Ожидайте обратной связи от админа"
    )
    await manager.switch_to(MoreFuncStates.menu)


async def coming_soon(
        callback: CallbackQuery,
        *_args: Any
) -> None:
    await callback.answer(
        "В разработке... 🛠",
        show_alert=True
    )
