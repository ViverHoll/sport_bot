from typing import TYPE_CHECKING

from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from app.models.enums import FavoritesEnum

if TYPE_CHECKING:
    from app.db import Database
    from app.models.dataclasses import UserType



async def clicked_favorites_on_post(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager,
) -> None:
    db: Database = manager.middleware_data["db"]
    user: UserType = manager.middleware_data["user"]

    favorite = await db.favorite.get_favorite_by_post_id(
        post_id=user.current_post,
        user_id=user.user_id,
    )

    if favorite:
        await db.favorite.delete_favorite(
            post_id=user.current_post,
            user_id=user.user_id,
        )
        await callback.answer("Удалено из избранного")
        manager.dialog_data["favorite_stars"] = "⭐️"
    else:
        await db.favorite.add_favorite(
            user_id=user.user_id,
            type=FavoritesEnum.POST,
            post_id=user.current_post
        )
        await callback.answer("Добавлено в избранное")
        manager.dialog_data["favorite_stars"] = "🌟"



async def clicked_like(
        _: CallbackQuery,
        __: Button,
        manager: DialogManager,
) -> None:
    db: Database = manager.middleware_data["db"]
    user: UserType = manager.middleware_data["user"]

    parameters = {
        "user_id": user.user_id,
        "post_id": user.current_post,
    }

    like = await db.like.get_like_by_ids(**parameters)
    post = await db.post.get_post_by_id(post_id=user.current_post)

    if like:
        await db.like.delete_like(**parameters)
        await db.post.update_post_by_id(
            post_id=user.current_post,
            likes=post.likes - 1,
        )
        manager.dialog_data["like"] = False
    else:
        await db.like.add_like(**parameters)
        await db.post.update_post_by_id(
            post_id=user.current_post,
            likes=post.likes + 1,
        )
        manager.dialog_data["like"] = True


