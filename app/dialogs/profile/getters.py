from datetime import datetime
from typing import Any

from aiogram_dialog import DialogManager

from app.entities.dataclasses import UserType


async def getter(
        dialog_manager: DialogManager,
        user: UserType,
        **_: Any,
) -> dict[str, Any]:
    checked = dialog_manager.dialog_data.get("is_checked", False)
    premium_options = ["Куплена", "Отсутствует"]
    notifications_options = ["Выключены", "Включены"]

    count_days = datetime.now().date() - user.created.date()

    return {
        "checked": checked,
        "not_checked": not checked,
        "user_id": user.user_id,
        "premium_status": premium_options[user.premium],
        "premium": user.premium,
        "created_date": user.created.date(),
        "count_days": count_days.days,
        "notifications_status": notifications_options[checked],
    }
