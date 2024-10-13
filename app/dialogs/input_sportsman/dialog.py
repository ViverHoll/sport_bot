from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Column, SwitchTo
from aiogram_dialog.widgets.text import Const

from app.dialogs.states import InputSportsman

from .handlers import get_file_handler

input_sportsman_dialog = Dialog(
    Window(
        Const("Как будете добавлять спортсмена?"),
        Column(
            Button(
                text=Const("Текст"),
                id="button_add_sportsman_text"
            ),
            SwitchTo(
                text=Const("Файл"),
                id="button_add_sportsman_file",
                state=InputSportsman.file
            )
        ),
        state=InputSportsman.select_options
    ),
    Window(
        Const("Пришлите файл с расширением .txt"),
        MessageInput(
            func=get_file_handler,
            content_types=ContentType.DOCUMENT
        ),
        state=InputSportsman.file
    )
)
