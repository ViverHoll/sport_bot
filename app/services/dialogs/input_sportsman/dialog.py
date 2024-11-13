from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput, TextInput
from aiogram_dialog.widgets.kbd import Button, Column, SwitchTo
from aiogram_dialog.widgets.text import Const

from app.services.dialogs.states import InputSportsman

from .handlers import get_file_handler

input_sportsman_dialog = Dialog(
    Window(
        Const("Отправьте имя спортсмена:"),
        TextInput(
            id="input_sportsman",
            on_success=...,
        ),
        state=InputSportsman.name,
    )
)
