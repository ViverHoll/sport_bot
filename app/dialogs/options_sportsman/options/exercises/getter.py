from typing import Any, TYPE_CHECKING

from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId

from app.models.dataclasses import UserType

if TYPE_CHECKING:
    from app.db import HolderDAO


async def get_more_exercises(
        dialog_manager: DialogManager,
        user: UserType,
        **_kwargs: Any,
) -> dict[str, Any]:
    db: HolderDAO = dialog_manager.middleware_data["db"]
    sportsman = await db.athletes.get_sportsman_by_id(user.current_sportsman)

    sportsman_photo_url = MediaAttachment(
        ContentType.VIDEO,
        file_id=MediaId(
            file_id=sportsman.photo_url,
        ),
    )

    return {
        "sportsman_photo_url": sportsman_photo_url,
        "exercises": sportsman.exercises,
    }
