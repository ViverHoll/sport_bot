from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import OptionsSearchSportsman

from .getters import get_not_found_sportsman
from .handlers import get_input_name

window_name = Window(
    Const("Введите имя спортсмена:"),
    SwitchTo(
        text=Const("◀️"),
        id="button_back",
        state=OptionsSearchSportsman.categories,
    ),
    TextInput(
        id="input_name_sportsman",
        on_success=get_input_name,
    ),
    state=OptionsSearchSportsman.name,
)


not_found_sportsman_window = Window(
    Format(
        'К сожалению спортсмен "{sportsman}" не найден',
    ),
    SwitchTo(
        text=Const("Попробовать еще раз"),
        id="switch_to_try_again",
        state=OptionsSearchSportsman.categories,
    ),
    state=OptionsSearchSportsman.not_found,
    getter=get_not_found_sportsman,
)







