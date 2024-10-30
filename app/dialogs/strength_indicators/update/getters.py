from typing import Any, TYPE_CHECKING


from aiogram_dialog import DialogManager
from app.db import Database

if TYPE_CHECKING:
    from app.models.dataclasses import UserType


async def get_all_exercises(
        dialog_manager: DialogManager,
        **_kwargs: Any,
) -> dict[str, Any]:
    db: Database = dialog_manager.middleware_data["db"]
    user: UserType = dialog_manager.middleware_data["user"]

    exercises = await db.strength_indicator.get_all_strength_indicators(
        user_id=user.user_id,
    )

    return {
        "exercises": [
            (
                exercise.name,
                exercise.id,
            )
            for exercise in exercises
        ],
        "pages": 1,
    }


async def get_exercise_info(
        dialog_manager: DialogManager,
        db: Database,
        **_kwargs: Any,
) -> dict[str, Any]:
    exercise_info = await db.strength_indicator.get_by_id(
        exercise_id=dialog_manager.dialog_data["exercise_id"],
    )
    return {
        "exercise_info": f"Название: {exercise_info.name}\n"
                         f"Силовые: {exercise_info.core}",
    }


async def get_data(
        dialog_manager: DialogManager,
        db: Database,
        **_kwargs: Any,
) -> dict[str, Any]:
    exercise_info = await db.strength_indicator.get_by_id(
        exercise_id=dialog_manager.dialog_data["exercise_id"],
    )
    return {
        "old_exercise_info": f"Название: {exercise_info.name}\n"
                             f"Силовые: {exercise_info.core}",
        "new_exercise_info": f"Название: {exercise_info.name}\n"
                             f"Силовые: {dialog_manager.dialog_data["exercise_core"]}",
    }
