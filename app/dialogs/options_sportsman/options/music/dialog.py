from aiogram import F
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Group, Start, SwitchTo
from aiogram_dialog.widgets.text import Const

from app.dialogs.states import Music, OptionsSportsmanStates, Pay

music_sportsman_dialog = Dialog(
    Window(
        Const("Он любил слушать разную музыку, в основном слушал фонк"),
        Group(
            SwitchTo(
                text=Const("🎵 1 трек"),
                id="button_one_music",
                state=Music.one_item
            ),
            SwitchTo(
                text=Const("🎶 Все треки"),
                id="button_all_music",
                state=Music.more_item
            ),
            Start(
                text=Const("⬅️ Назад"),
                id="button_back",
                state=OptionsSportsmanStates.options
            ),
            width=2
        ),
        state=Music.select
    ),
    Window(
        Const("Тут 1 трек спортсмена"),
        Start(
            text=Const("💵 Купить подписку"),
            id="button_pay_sub",
            state=Pay.menu,
            when=~F["premium"]
        ),
        SwitchTo(
            text=Const("⬅️ Назад"),
            id="button_back",
            state=Music.select
        ),
        state=Music.one_item
    ),
    Window(
        Const("Тут все треки спортсмена"),
        SwitchTo(
            text=Const("⬅️ Назад"),
            id="back_to_select_menu",
            state=Music.select
        ),
        state=Music.more_item
    )
)
