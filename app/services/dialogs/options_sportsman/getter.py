from typing import Any

from aiogram.enums import ContentType
from aiogram_dialog.api.entities import MediaAttachment, MediaId

from app.models.dataclasses import UserType
from app.services.db import Database


async def get_info_about_sportsman(
        user: UserType,
        db: Database,
        **_kwargs: Any,
) -> dict[str, Any]:
    info_sportsman = await db.athletes.get_sportsman_by_id(user.current_sportsman)

    sportsman_photo_url = MediaAttachment(
        ContentType.PHOTO,
        file_id=MediaId(
            file_id=info_sportsman.photo_url,
        ),
    )

    return {
        "sportsman_full_name": info_sportsman.full_name,
        "sportsman_photo_url": sportsman_photo_url,
        "nickname": info_sportsman.nickname,
    }
