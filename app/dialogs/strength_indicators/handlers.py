from typing import TYPE_CHECKING

from aiogram.types import Message, CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput

from app.dialogs.states import NewStrengthIndicators, ProfileDialog

if TYPE_CHECKING:
    from app.db import HolderDAO


async def get_name_exercises(
        _: Message,
        __: ManagedTextInput,
        manager: DialogManager,
        text: str
) -> None:
    manager.dialog_data["name_exercises"] = text

    await manager.switch_to(
        state=NewStrengthIndicators.core
    )


async def get_core_exercises(
        _: Message,
        __: ManagedTextInput,
        manager: DialogManager,
        text: str
) -> None:
    manager.dialog_data["core_exercises"] = text

    await manager.switch_to(
        state=NewStrengthIndicators.confirm
    )


async def save_new_strength_indicators(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager
) -> None:
    db: HolderDAO = manager.middleware_data["db"]
    name = manager.dialog_data.get("name_exercises")
    core = manager.dialog_data.get("core_exercises")

    await db.strength_indicator.add_strength_indicators(
        user_id=callback.from_user.id,
        name=name,
        core=core
    )
    await callback.message.answer("Упражнение успешно сохранено")
    await manager.start(ProfileDialog.menu)
