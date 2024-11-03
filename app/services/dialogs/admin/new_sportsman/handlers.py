from aiogram.types import Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

from app.services.dialogs.states import NewSportsmanDialog

async def get_name_sportsman(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        name: str,
) -> None:
    manager.dialog_data["name_sportsman"] = name

    await manager.switch_to(
        state=NewSportsmanDialog.surname,
    )


async def get_surname_sportsman(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        surname: str,
) -> None:
    manager.dialog_data["surname_sportsman"] = surname

    await manager.switch_to(
        state=NewSportsmanDialog.description,
    )


async def get_description_sportsman(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        description: str,
) -> None:
    manager.dialog_data["description_sportsman"] = description

    await manager.switch_to(
        state=NewSportsmanDialog.photo,
    )


async def get_name_sportsman(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        name: str,
) -> None:
    manager.dialog_data["name_sportsman"] = name

    await manager.switch_to(
        state=NewSportsmanDialog.surname,
    )


async def get_name_sportsman(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        name: str,
) -> None:
    manager.dialog_data["name_sportsman"] = name

    await manager.switch_to(
        state=NewSportsmanDialog.surname,
    )


async def get_name_sportsman(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        name: str,
) -> None:
    manager.dialog_data["name_sportsman"] = name

    await manager.switch_to(
        state=NewSportsmanDialog.surname,
    )


async def get_name_sportsman(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        name: str,
) -> None:
    manager.dialog_data["name_sportsman"] = name

    await manager.switch_to(
        state=NewSportsmanDialog.surname,
    )


async def get_name_sportsman(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        name: str,
) -> None:
    manager.dialog_data["name_sportsman"] = name

    await manager.switch_to(
        state=NewSportsmanDialog.surname,
    )
