from typing import Any

from aiogram.enums.content_type import ContentType

from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId

from app.services.db import Database
from app.models.dataclasses import UserType


async def get_info_post(
        dialog_manager: DialogManager,
        db: Database,
        user: UserType,
        **_kwargs: Any,
) -> dict[str, Any]:
    """
    :param dialog_manager: Менеджер Диалогов
    :param db: База данных
    :param user: Модель юзера(dto)
    :param _kwargs: Другие параметры, которые не нужны
    :return: dict[str, Any]
    """
    posts = await db.post.get_all_posts(
        user_id=user.user_id,
    )
    current_page = await dialog_manager.find("scroll_delete_post").get_page()
    current_post = posts[current_page]

    post_photo = MediaAttachment(
        type=ContentType.PHOTO,
        file_id=MediaId(
            file_id=current_post.media,
        ),
    )

    await db.users.update_user(
        user_id=user.user_id,
        current_post=current_post.post_id,
    )

    return {
        "posts": len(posts),
        "description": current_post.description,
        "tags": current_post.tags,
        "post_photo": post_photo,
    }
