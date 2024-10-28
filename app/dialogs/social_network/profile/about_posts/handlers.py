from typing import TYPE_CHECKING

from aiogram import Bot
from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

if TYPE_CHECKING:
    from app.db import Database


async def send_user_posts(
        callback: CallbackQuery,
        _: Button,
        manager: DialogManager
) -> None:
    db: Database = manager.middleware_data["db"]
    bot: Bot = manager.middleware_data["bot"]

    posts = await db.post.get_all_posts(callback.from_user.id)
    for post in posts:
        tags = post.tags if post.tags else ""
        await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=post.media,
            caption=f"{post.description}\n\n{tags}"
        )
