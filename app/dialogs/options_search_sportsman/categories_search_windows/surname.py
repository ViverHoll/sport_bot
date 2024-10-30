from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const

from app.dialogs.states import OptionsSearchSportsman

from .handlers import get_input_surname

window_surname = Window(
    Const("Введите фамилию спортсмена:"),
    SwitchTo(
        text=Const("◀️ Назад"),
        id="button_back",
        state=OptionsSearchSportsman.categories,
    ),
    TextInput(
        id="input_surname_sportsman",
        on_success=get_input_surname,
    ),
    state=OptionsSearchSportsman.surname,
)
