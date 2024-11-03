from typing import Any, TYPE_CHECKING

from aiogram_dialog import DialogManager

if TYPE_CHECKING:
    from app.services.db import HolderDAO


async def get_list_sportsman(
        dialog_manager: DialogManager,
        **_kwargs: Any,
) -> dict[str, Any]:
    db: HolderDAO = dialog_manager.middleware_data["db"]
    sportsman_list = await db.athletes.get_athletes()

    return {
        "athletes": [
            (
                f"{sportsman.get_full_name()}\n"
                f"<i>{sportsman.description}</i>\n\n",
                sportsman.sportsmen_id,
            )
            for sportsman in sportsman_list
        ],
        "count_athletes": len(sportsman_list),
        "athletes_names": [
            (sportsman.get_full_name(), sportsman.sportsmen_id)
            for sportsman in sportsman_list
        ],
    }
