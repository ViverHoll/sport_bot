from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import Column, Row, SwitchTo, Start, NextPage, CurrentPage, PrevPage, Row
from aiogram_dialog.widgets.text import Const, List, Format

from app.dialogs.states import OptionsSearchSportsman, StubScrollSportsman

from .categories_search_windows import (
    window_genre_musix,
    window_name,
    window_surname,
)

from .getters import get_list_sportsman

options_search_dialog = Dialog(
    Window(
        Const("Как будете искать спортсмена?"),
        Start(
            text=Const("Меню спортсменов"),
            id="button_auto_search",
            state=StubScrollSportsman.sportsman,
            mode=StartMode.RESET_STACK
        ),
        SwitchTo(
            text=Const("Список спортсменов"),
            id="switch_to_list_sportsman",
            state=OptionsSearchSportsman.list_sportsman
        ),
        SwitchTo(
            text=Const("Ручной поиск"),
            id="button_self_search",
            state=OptionsSearchSportsman.categories
        ),
        state=OptionsSearchSportsman.select
    ),
    Window(
        Const("По какому параметру будет поиск?"),
        Row(
            SwitchTo(
                text=Const("🗣 Имя"),
                id="search_by_name",
                state=OptionsSearchSportsman.name
            ),
            SwitchTo(
                text=Const("✍️ Фамилия"),
                id="search_by_surname",
                state=OptionsSearchSportsman.surname
            )
        ),
        Column(
            SwitchTo(
                text=Const("🎧 Жанр музыки"),
                id="search_by_genre_music",
                state=OptionsSearchSportsman.genre_music
            ),
        ),
        SwitchTo(
            text=Const("◀️ Назад"),
            id="button_back",
            state=OptionsSearchSportsman.select
        ),
        state=OptionsSearchSportsman.categories
    ),
    Window(
        Const("<b>Список спортсменов:</b>"),
        List(
            field=Format(
                "{pos}. {item[0]}"),
            items="athletes",
            id="scroll_list_sportsman",
            page_size=5
        ),
        Row(
            PrevPage(
                scroll="scroll_list_sportsman",
                text=Const("⬅️")
            ),
            CurrentPage(
                scroll="scroll_list_sportsman"
            ),
            NextPage(
                scroll="scroll_list_sportsman",
                text=Const("➡️")
            )
        ),
        state=OptionsSearchSportsman.list_sportsman,
        getter=get_list_sportsman
    ),
    window_surname,
    window_genre_musix,
    window_name
)



