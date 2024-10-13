from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput


async def search_available(
        callback: CallbackQuery,
        *_: Any
) -> None:
    await callback.answer(
        "Поиск пока недоступен.",
        show_alert=True
    )


async def get_input_name(
        message: Message,
        _: ManagedTextInput,
        manager: DialogManager,
        __: str
) -> None:
    await message.answer(
        "Данные не найдены. Попробуйте позже"
    )
    await manager.done()
