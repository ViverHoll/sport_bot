from datetime import datetime
from typing import Any

from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId

from app.entities.dataclasses import UserType

"""strength indicators"""


def _get_photo_for_aiogram_dialog(
        *,
        photo_id: str,
        content_type: ContentType
) -> MediaAttachment:
    return MediaAttachment(
        type=content_type,
        file_id=MediaId(
            file_id=photo_id
        )
    )


async def getter(
        dialog_manager: DialogManager,
        user: UserType,
        **_: Any,
) -> dict[str, Any]:
    checked = dialog_manager.dialog_data.get("is_checked", False)
    premium_options = ["Куплена", "Отсутствует"]
    notifications_options = ["Выключены", "Включены"]

    count_days = datetime.now().date() - user.created.date()

    if user.user_photo:
        photo = _get_photo_for_aiogram_dialog(
            photo_id=user.user_photo,
            content_type=ContentType.PHOTO
        )
        button_photo_name = "Изменить фото"
    else:
        button_photo_name = "Добавить фото"
        photo = False

    return {
        "checked": checked,
        "not_checked": not checked,
        "user_id": user.user_id,
        "premium_status": premium_options[user.premium],
        "premium": user.premium,
        "created_date": user.created.date(),
        "count_days": count_days.days,
        "notifications_status": notifications_options[checked],
        "count_gym_bro": 32,
        "button_photo_name": button_photo_name,
        "photo_user": photo
    }
