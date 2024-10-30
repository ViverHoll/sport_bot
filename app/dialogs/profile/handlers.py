from typing import Any, TYPE_CHECKING

from aiogram.types import CallbackQuery, Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import ManagedCheckbox
from aiogram_dialog.widgets.input import MessageInput

from app.dialogs.states import ProfileDialog
from app.models.dataclasses import UserType

if TYPE_CHECKING:
    from app.db import HolderDAO


async def clicked_on_notifications(
        _: CallbackQuery,
        checkbox: ManagedCheckbox,
        manager: DialogManager,
) -> None:
    manager.dialog_data.update(
        is_checked=checkbox.is_checked(),
    )


async def coming_soon(
        callback: CallbackQuery,
        *_args: Any,
) -> None:
    await callback.answer(
        "В разработке... 🛠",
        show_alert=True,
    )


async def get_new_photo_user(
        message: Message,
        _: MessageInput,
        manager: DialogManager,
) -> None:
    db: HolderDAO = manager.middleware_data["db"]
    user: UserType = manager.middleware_data["user"]
    user.user_photo = message.photo[-1].file_id

    await db.users.update_user(
        user_id=message.from_user.id,
        user_photo=message.photo[-1].file_id,
    )
    await message.answer(
        "Фото успешно обновлено",
    )
    await manager.switch_to(
        state=ProfileDialog.menu,
    )

