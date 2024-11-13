from typing import Any

from aiogram_dialog import DialogManager


async def get_info_admin_getter(
        dialog_manager: DialogManager,
        **_kwargs: Any,
) -> dict[str, str | int]:
    admin_id, name, *_ = dialog_manager.dialog_data.values()
    return {
        "admin_id": admin_id,
        "name": name,
    }
