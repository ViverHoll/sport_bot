from typing import TYPE_CHECKING

from aiogram.types import CallbackQuery, Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select, Button
from aiogram_dialog.widgets.input import ManagedTextInput

from app.dialogs.states import UpdateStrengthIndicator

if TYPE_CHECKING:
    from app.entities.dataclasses import UserType
    from app.db import Database


async def get_select_exercise(
        _: CallbackQuery,
        widget: Select,
        manager: DialogManager,
        button_id: int
) -> None:
    manager.dialog_data["exercise_id"] = button_id

    await manager.switch_to(
        state=UpdateStrengthIndicator.new_core
    )


async def get_new_input_strength_indicator(
        _: Message,
        __: ManagedTextInput,
        manager: DialogManager,
        text: str
) -> None:
    manager.dialog_data["exercise_core"] = text
    await manager.switch_to(
        state=UpdateStrengthIndicator.confirm
    )


async def update_strength_indicator(
        callback: CallbackQuery,
        _: Button,
        manager: DialogManager
) -> None:
    db: Database = manager.middleware_data["db"]
    user: UserType = manager.middleware_data["user"]

    await db.strength_indicator.update_by_exercise_id(
        user_id=user.user_id,
        exercise_id=manager.dialog_data["exercise_id"],
        core=manager.dialog_data["exercise_core"]
    )
    await callback.answer("Успешно!")
