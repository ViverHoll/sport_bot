from typing import Any

from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import ManagedCheckbox


async def clicked_on_notifications(
        _: CallbackQuery,
        checkbox: ManagedCheckbox,
        manager: DialogManager
) -> None:
    manager.dialog_data.update(
        is_checked=checkbox.is_checked()
    )


async def coming_soon(
        callback: CallbackQuery,
        *_args: Any
) -> None:
    await callback.answer(
        "В разработке... 🛠",
        show_alert=True
    )
