from typing import Any

from aiogram_dialog import DialogManager


async def get_exercises(
        dialog_manager: DialogManager,
        **_kwargs: Any,
) -> dict[str, Any]:
    dialog_data = dialog_manager.dialog_data
    return {
        "name_exercises": dialog_data.get("name_exercises"),
        "core_exercises": dialog_data.get("core_exercises"),
    }
