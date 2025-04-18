from typing import Final

from aiogram.enums.content_type import ContentType

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import (
    Button, Next, Column,
)

from app.services.dialogs.states import NewSportsmanDialog

from .handlers import (
    get_name_sportsman,
    get_surname_sportsman,
    get_description_sportsman,
    get_photo_sportsman,
    get_nickname_sportsman,
    get_exercises_sportsman,
    get_food_sportsman,
    get_music_sportsman,
    cancel_add_new_sportsman,
    success_confirm_add_new_sportsman,
)

stop_button: Final[Button] = Button(
    text=Const("Прекратить"),
    id="stop_input_sportsman",
    on_click=cancel_add_new_sportsman,
)

# skip_button: Final[Button] = Button(
#     text=Const("Пропустить"),
#     id="skip_button",
#     on_click=...
# )

skip_step = Next(
    text=Const("Пропустить"),
)

new_sportsman_dialog = Dialog(
    Window(
        Const("Введите имя спортсмена:"),
        TextInput(
            id="input_name_new_sportsman",
            on_success=get_name_sportsman,
        ),
        stop_button,
        state=NewSportsmanDialog.name,
    ),
    Window(
        Const("Введите фамилию:"),
        TextInput(
            id="input_surname_new_sportsman",
            on_success=get_surname_sportsman,
        ),
        stop_button,
        state=NewSportsmanDialog.surname,
    ),
    Window(
        Const("Введите описание спортсмена:"),
        TextInput(
            id="input_description_new_sportsman",
            on_success=get_description_sportsman,
        ),
        stop_button,
        state=NewSportsmanDialog.description,
    ),
    Window(
        Const("Отправьте фотку спортсмена:"),
        MessageInput(
            func=get_photo_sportsman,
            content_types=ContentType.PHOTO,
        ),
        stop_button,
        state=NewSportsmanDialog.photo,
    ),
    Window(
        Const('Введите "прозвище" спортсмена'),
        TextInput(
            id="input_nickname_new_sportsman",
            on_success=get_nickname_sportsman,
        ),
        Column(
            stop_button,
            skip_step,
        ),
        state=NewSportsmanDialog.nickname,
    ),
    Window(
        Const("Введите программу спортсмена:"),
        TextInput(
            id="input_exercises_new_sportsman",
            on_success=get_exercises_sportsman,
        ),
        Column(
            stop_button,
            skip_step,
        ),
        state=NewSportsmanDialog.exercises,
    ),
    Window(
        Const("Введите план питания спортсмена:"),
        TextInput(
            id="input_food_new_sportsman",
            on_success=get_food_sportsman,
        ),
        Column(
            stop_button,
            skip_step,
        ),
        state=NewSportsmanDialog.food,
    ),
    Window(
        Const("Введите музыку которую слушает спортсмен:"),
        TextInput(
            id="input_music_new_sportsman",
            on_success=get_music_sportsman,
        ),
        Column(
            stop_button,
            skip_step,
        ),
        state=NewSportsmanDialog.music,
    ),
    Window(
        Format("ДАННЫЕ"),
        Column(
            Button(
                text=Const("Подтвердить"),
                id="confirm_sportsman",
                on_click=success_confirm_add_new_sportsman,
            ),
            Button(
                text=Const("Отменить"),
                id="not_confirm_sportsman",
                on_click=cancel_add_new_sportsman,
            ),
        ),
        state=NewSportsmanDialog.confirm,
    ),
)
