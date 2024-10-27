from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import (
    Button,
    Group,
    NextPage,
    PrevPage,
    Row,
    StubScroll,
    Start,
)
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.select_sportsman.handlers import (
    paging_logic,
    select_current_sportsman,
)
from app.dialogs.states import StubScrollSportsman, OptionsSearchSportsman

scroll_sportsman_dialog = Dialog(
    Window(
        DynamicMedia("sportsman_photo_url"),
        Format(
            "<b><i>{sportsman_full_name}</i></b>\n\n"
            "<i>{bio_sportsman}</i>\n\n"
            # "🙊 Прозвище: {nickname}\n\n"
            # "🎊 Дата рождения: {years_life}\n\n"
            # "📏 Рост: {height} см\n\n"
        ),
        StubScroll(
            id="stub_scroll",
            pages="pages"
        ),
        Group(
            Button(
                text=Const("⭐️ Добавить в избранное"),
                id="button_adding_sportsman_in_favorites"
            ),
            width=1
        ),
        Row(
            PrevPage(
                scroll="stub_scroll",
                text=Const("⬅️")
            ),
            Button(
                text=Const("✅"),
                id="select_scroll_sportsman",
                on_click=select_current_sportsman
            ),
            NextPage(
                scroll="stub_scroll",
                text=Const("➡️")
            ),
        ),
        Start(
            text=Const("⬅️ Вернуться назад"),
            id="back_to_select_sportsman",
            state=OptionsSearchSportsman.select
        ),
        state=StubScrollSportsman.sportsman,
        getter=paging_logic,
        # parse_mode="html"
    ),
)

"""220"""
"""86"""

"""133"""
"""65"""
