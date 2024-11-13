from typing import TYPE_CHECKING

from aiogram.types import Message, CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from app.services.dialogs.states import NewAdminDialog

if TYPE_CHECKING:
    from app.services.db import Database


def check_admin_id(text: str) -> int:
    """
    Проверка id нового админа. Если введено не число, то выбрасывается исключение.
    :param text: Id admin.
    :return: Int id admin.
    """
    return int(text)


async def get_id_new_admin(
        _: Message,
        __: ManagedTextInput,
        manager: DialogManager,
        admin_id: int,
) -> None:
    """Получение id нового админа."""
    manager.dialog_data["admin_id"] = admin_id
    await manager.switch_to(NewAdminDialog.name)


async def get_name_new_admin(
        _: Message,
        __: ManagedTextInput,
        manager: DialogManager,
        name: str,
) -> None:
    """Получение имени нового админа."""
    manager.dialog_data["name"] = name
    await manager.switch_to(NewAdminDialog.confirm)


async def success_confirm_new_admin(
        callback: CallbackQuery,
        _: Button,
        manager: DialogManager,
) -> None:
    """Соглашение добавить админа."""
    db: Database = manager.middleware_data["db"]
    await db.admin.add_admin(
        admin_id=manager.dialog_data["admin_id"],
        name=manager.dialog_data["name"],
    )

    await callback.answer("Успешно!")
    await manager.done()


async def cancel_new_admin(
        callback: CallbackQuery,
        _: Button,
        manager: DialogManager,
) -> None:
    """Отмена добавления админа."""
    await callback.answer("Отменено")
    await manager.done()
