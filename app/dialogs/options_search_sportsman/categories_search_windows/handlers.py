from typing import TYPE_CHECKING

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

from app.dialogs.states import OptionsSportsmanStates, OptionsSearchSportsman

if TYPE_CHECKING:
    from app.db import Database
    from app.models.dataclasses import UserType


async def get_input_name(
        message: Message,
        _: ManagedTextInput,
        manager: DialogManager,
        name_sportsman: str,
) -> None:
    db: Database = manager.middleware_data["db"]
    user: UserType = manager.middleware_data["user"]

    sportsman = await db.athletes.get_sportsman_by_name(name_sportsman)
    if sportsman:
        await db.users.update_user(
            user_id=user.user_id,
            current_sportsman=sportsman.sportsmen_id,
        )
        await manager.start(OptionsSportsmanStates.options)
    else:
        manager.dialog_data["not_found_sportsman"] = name_sportsman
        await manager.switch_to(OptionsSearchSportsman.not_found)


async def get_input_surname(
        message: Message,
        _: ManagedTextInput,
        manager: DialogManager,
        surname_sportsman: str,
) -> None:
    db: Database = manager.middleware_data["db"]
    user: UserType = manager.middleware_data["user"]

    sportsman = await db.athletes.get_sportsman_by_surname(surname_sportsman)
    if sportsman:
        await db.users.update_user(
            user_id=user.user_id,
            current_sportsman=sportsman.sportsmen_id,
        )
        await manager.start(OptionsSportsmanStates.options)
    else:
        manager.dialog_data["not_found_sportsman"] = surname_sportsman
        await manager.switch_to(OptionsSearchSportsman.not_found)

