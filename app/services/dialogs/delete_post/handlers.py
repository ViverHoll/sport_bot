from typing import TYPE_CHECKING

from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from app.services.dialogs.states import SocialNetworkProfile

if TYPE_CHECKING:
    from app.services.db import Database
    from app.models.dataclasses import UserType


async def delete_post_handler(
        callback: CallbackQuery,
        _: Button,
        manager: DialogManager,
) -> None:
    db: Database = manager.middleware_data["db"]
    user: UserType = manager.middleware_data["user"]

    await db.post.delete_post(
        post_id=user.current_post,
    )
    await callback.answer(
        "Пост успешно удален",
    )
    await manager.start(state=SocialNetworkProfile.options)
