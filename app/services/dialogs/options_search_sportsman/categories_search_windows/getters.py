from typing import Any

from aiogram_dialog import DialogManager


async def get_not_found_sportsman(
        dialog_manager: DialogManager,
        **_kwargs: Any,
) -> dict[str, str]:
    return {
        "sportsman": dialog_manager.dialog_data["not_found_sportsman"],
    }



