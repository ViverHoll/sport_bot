from typing import Any, TYPE_CHECKING

from aiogram_dialog import DialogManager

if TYPE_CHECKING:
    from app.db import HolderDAO


async def get_list_sportsman(
        dialog_manager: DialogManager,
        **_kwargs: Any
) -> dict[str, Any]:
    db: HolderDAO = dialog_manager.middleware_data["db"]
    sportsman_list = await db.athletes.get_athletes()

    return {
        "athletes": [
            (
                f"<b>{sportsman.full_name()}</b>\n"
                f"<i>{sportsman.description}</i>\n\n",
                count
            )
            for count, sportsman in enumerate(sportsman_list, 1)
        ],
        "count_athletes": len(sportsman_list)
    }
