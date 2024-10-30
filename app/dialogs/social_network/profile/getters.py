from typing import Any, TYPE_CHECKING

from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId

from app.models.dataclasses import UserType

if TYPE_CHECKING:
    from app.db import HolderDAO


async def get_data_user(
        dialog_manager: DialogManager,
        user: UserType,
        **_kwargs: Any,
) -> dict[str, Any]:
    db: HolderDAO = dialog_manager.middleware_data["db"]
    user_social_network = await db.social_network.get_user_by_id(
        user_id=user.user_id,
    )

    user_media = MediaAttachment(
        ContentType.PHOTO,
        file_id=MediaId(
            file_id=user_social_network.media,
        ),
    )

    return {
        "media": user_media,
        "full_name": user_social_network.full_name,
        "age": user_social_network.age,
        "description": user_social_network.description,
        "city": user_social_network.city,
        "likes": user_social_network.likes,
    }
