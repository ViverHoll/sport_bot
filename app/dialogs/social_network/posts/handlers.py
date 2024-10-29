from typing import TYPE_CHECKING

from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

if TYPE_CHECKING:
    from app.db import Database
    from app.models.dataclasses import UserType


async def clicked_like(
        _: CallbackQuery,
        __: Button,
        manager: DialogManager
) -> None:
    db: Database = manager.middleware_data["db"]
    user: UserType = manager.middleware_data["user"]

    parameters = {
        "user_id": user.user_id,
        "post_id": user.current_post
    }

    like = await db.like.get_like_by_ids(**parameters)
    post = await db.post.get_post_by_id(post_id=user.current_post)

    if like:
        await db.like.delete_like(**parameters)
        await db.post.update_post_by_id(
            post_id=user.current_post,
            likes=post.likes - 1
        )
        manager.dialog_data["like"] = False
    else:
        await db.like.add_like(**parameters)
        await db.post.update_post_by_id(
            post_id=user.current_post,
            likes=post.likes + 1
        )
        manager.dialog_data["like"] = True
