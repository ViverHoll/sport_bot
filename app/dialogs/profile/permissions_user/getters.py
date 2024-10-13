from typing import Any

from aiogram_dialog import DialogManager


async def get_settings_statuses(
        dialog_manager: DialogManager,
        **_kwargs: Any,
) -> dict[str, Any]:
    notifications_status = dialog_manager.dialog_data.get("notifications", False)
    motivation_status = dialog_manager.dialog_data.get("motivation_quotes", False)
    grade_status = dialog_manager.dialog_data.get("grade", False)
    gym_bro_status = dialog_manager.dialog_data.get("search_gym_bro", False)

    notifications_options = ["Выключены", "Включены"]
    motivation_quotes = ["Не получать", "Получать"]
    show_grade_options = ["Не показывать", "Показывать"]
    search_gym_bro_options = ["Не искать", "Искать"]

    return {
        "notifications_status": notifications_options[notifications_status],
        "motivation_status": motivation_quotes[motivation_status],
        "grade_status": show_grade_options[grade_status],
        "gym_status": search_gym_bro_options[gym_bro_status]
    }
