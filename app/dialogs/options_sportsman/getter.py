from typing import Any, TYPE_CHECKING

from aiogram.types import User
from aiogram_dialog import DialogManager
from aiogram.enums import ContentType
from aiogram_dialog.api.entities import MediaAttachment, MediaId

if TYPE_CHECKING:
    from app.db import HolderDAO


async def get_info_about_sportsman(
        dialog_manager: DialogManager,
        event_from_user: User,
        **_: Any,
) -> dict[str, Any]:
    db: HolderDAO = dialog_manager.middleware_data["db"]
    user = await db.users.get_user(event_from_user.id)
    info_sportsman = await db.athletes.get_sportsman_by_id(user.current_sportsman)

    sportsman_photo_url = MediaAttachment(
        ContentType.PHOTO,
        file_id=MediaId(
            file_id=info_sportsman.photo_url,
        ),
    )

    return {
        "sportsman_full_name": info_sportsman.name + info_sportsman.surname,
        "sportsman_photo_url": sportsman_photo_url,
        "nickname": info_sportsman.nickname,
        "years_life": info_sportsman.years_life,
        "height": info_sportsman.height,
    }
