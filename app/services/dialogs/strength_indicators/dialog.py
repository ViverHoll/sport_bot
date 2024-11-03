from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Start

from app.services.dialogs.states import NewStrengthIndicators, ProfileDialog
from .handlers import (
    get_name_exercises,
    get_core_exercises,
    save_new_strength_indicators,
)
from .getters import get_exercises

strength_indicators = Dialog(
    Window(
        Const("Введите название упражнения:"),
        Start(
            text=Const("Главное меню"),
            id="button_go_to_back_profile",
            state=ProfileDialog.menu,
        ),
        TextInput(
            id="input_name_exercises",
            on_success=get_name_exercises,
        ),
        state=NewStrengthIndicators.name,
    ),
    Window(
        Const(
            "Отлично! Теперь введите силовые к этому упражнению.\n\n"
            "К примеру: 50кг на 3 раза",
        ),
        Start(
            text=Const("Главное меню"),
            id="button_go_to_back_profile",
            state=ProfileDialog.menu,
        ),
        TextInput(
            id="input_name_exercises",
            on_success=get_core_exercises,
        ),
        state=NewStrengthIndicators.core,
    ),
    Window(
        Format(
            "Название: {name_exercises}\n"
            "Силовые: {core_exercises}",
        ),
        Button(
            text=Const("Сохранить"),
            id="button_save_new_strength_indicators",
            on_click=save_new_strength_indicators,
        ),
        Start(
            text=Const("Главное меню"),
            id="go_to_back_profile_menu",
            state=ProfileDialog.menu,
        ),
        state=NewStrengthIndicators.confirm,
        getter=get_exercises,
    ),
)



