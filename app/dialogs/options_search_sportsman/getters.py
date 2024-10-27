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
    print(sportsman_list)

    return {
        "athletes": [
            (
                f"{sportsman.full_name()}\n"
                f"<i>{sportsman.description}</i>\n\n",
                sportsman.sportsmen_id
            )
            for sportsman in sportsman_list
        ],
        "count_athletes": len(sportsman_list),
        "athletes_names": [
            (sportsman.full_name(), sportsman.sportsmen_id)
            for sportsman in sportsman_list
        ]
    }
