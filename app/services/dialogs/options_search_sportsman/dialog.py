
from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import (
    Row, SwitchTo, Start,
)
from aiogram_dialog.widgets.text import Const

from app.services.dialogs.states import OptionsSearchSportsman, StubScrollSportsman

from .categories_search_windows import (
    window_name,
    window_surname,
    not_found_sportsman_window,
)


options_search_dialog = Dialog(
    Window(
        Const("Как будете искать спортсмена?"),
        Start(
            text=Const("Меню спортсменов"),
            id="button_auto_search",
            state=StubScrollSportsman.sportsman,
            mode=StartMode.RESET_STACK,
        ),
        SwitchTo(
            text=Const("Ручной поиск"),
            id="button_self_search",
            state=OptionsSearchSportsman.categories,
        ),
        state=OptionsSearchSportsman.select,
    ),
    Window(
        Const("По какому параметру будет поиск?"),
        Row(
            SwitchTo(
                text=Const("🗣 Имя"),
                id="search_by_name",
                state=OptionsSearchSportsman.name,
            ),
            SwitchTo(
                text=Const("✍️ Фамилия"),
                id="search_by_surname",
                state=OptionsSearchSportsman.surname,
            ),
        ),
        SwitchTo(
            text=Const("◀️ Назад"),
            id="button_back",
            state=OptionsSearchSportsman.select,
        ),
        state=OptionsSearchSportsman.categories,
    ),
    window_surname,
    window_name,
    not_found_sportsman_window,
)
