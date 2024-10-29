from typing import Any, TYPE_CHECKING

from aiogram_dialog import DialogManager

from app.models.dataclasses import UserType

if TYPE_CHECKING:
    from app.db import HolderDAO


async def get_more_foods(
        dialog_manager: DialogManager,
        user: UserType,
        **_kwargs: Any
) -> dict[str, Any]:
    db: HolderDAO = dialog_manager.middleware_data["db"]
    sportsman = await db.athletes.get_sportsman_by_id(user.current_sportsman)

    return {
        "food": sportsman.food
    }
