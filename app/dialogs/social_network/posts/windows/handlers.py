from typing import TYPE_CHECKING

from aiogram.types import Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

from app.dialogs.states import PostSocialNetwork

if TYPE_CHECKING:
    from aiogram import Bot

    from app.db import Database
    from app.models.dataclasses import UserType


async def get_input_comment(
        message: Message,
        __: ManagedTextInput,
        manager: DialogManager,
        comment: str
) -> None:
    db: Database = manager.middleware_data["db"]
    user: UserType = manager.middleware_data["user"]
    bot: Bot = manager.middleware_data["bot"]

    post_info = await db.post.get_post_by_id(
        post_id=user.current_post
    )

    await bot.send_message(
        chat_id=post_info.post_from_user,
        text=f"💬<b>Вам отправили комментарий:</b>\n\n"
             f"<i>{comment}</i>"
    )
    await message.answer("Ваш комментарий успешно отправлен!")
    await manager.switch_to(PostSocialNetwork.look_post)
