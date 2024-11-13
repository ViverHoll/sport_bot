from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Column

from app.services.dialogs.states import NewAdminDialog

from .getters import get_info_admin_getter
from .handlers import (
    check_admin_id,
    get_id_new_admin,
    get_name_new_admin,
    success_confirm_new_admin,
    cancel_new_admin,
)

new_admin_dialog = Dialog(
    Window(
        Const(
            "Введите айди нового админа:\n\n"
            "К примеру: 123456789",
        ),
        TextInput(
            id="input_id_new_admin",
            type_factory=check_admin_id,
            on_success=get_id_new_admin,
        ),
        state=NewAdminDialog.admin_id,
    ),
    Window(
        Const(
            "Введите имя нового админа:\n\n"
            "К примеру: Иван",
        ),
        TextInput(
            id="input_name_new_admin",
            on_success=get_name_new_admin,
        ),
        state=NewAdminDialog.name,
    ),
    Window(
        Format(
            "ID: {admin_id}\n"
            "Имя: {name}",
        ),
        Column(
            Button(
                text=Const("Подтвердить"),
                id="confirm_new_admin",
                on_click=success_confirm_new_admin,
            ),
            Button(
                text=Const("Отмена"),
                id="cancel_new_admin",
                on_click=cancel_new_admin,
            ),
        ),
        state=NewAdminDialog.confirm,
        getter=get_info_admin_getter,
    ),
)
