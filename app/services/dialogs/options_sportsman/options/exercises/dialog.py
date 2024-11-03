from aiogram import F
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Group, Start, SwitchTo
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from app.services.dialogs.options_sportsman.getter import get_info_about_sportsman
from .getter import get_more_exercises
from app.services.dialogs.states import Exercises, OptionsSportsmanStates, Pay
from .handlers import coming_soon

exercises_sportsman_dialog = Dialog(
    Window(
        DynamicMedia("sportsman_photo_url"),
        Const("Его любимым упражнением были подтягивания"),
        Group(
            Button(
                text=Const("🥱 1 упражнение"),
                id="button_one_exercises",
                on_click=coming_soon,
                # state=Exercises.one_item
            ),
            SwitchTo(
                text=Const("🤤 Все упражнения"),
                id="button_all_exercises",
                state=Exercises.more_item,
            ),
            Start(
                text=Const("⬅️ Назад"),
                id="button_back",
                state=OptionsSportsmanStates.options,
            ),
            width=2,
        ),
        state=Exercises.select,
        getter=get_info_about_sportsman,
    ),
    Window(
        Const("Подтягивания\n\nТут информация и техника"),
        Start(
            text=Const("💵 Купить подписку"),
            id="button_pay_sub",
            state=Pay.menu,
            when=~F["premium"],
        ),
        SwitchTo(
            text=Const("⬅️ Назад"),
            id="button_back",
            state=Exercises.select,
        ),
        state=Exercises.one_item,
        getter=get_info_about_sportsman,
    ),
    Window(
        Format("{exercises}"),
        # SwitchTo(
        #     text=Const("⬅️ Назад"),
        #     id="button_back",
        #     state=Exercises.select
        # ),
        Start(
            text=Const("⬅️ Назад"),
            id="button_back",
            state=OptionsSportsmanStates.options,
        ),
        state=Exercises.more_item,
        getter=get_more_exercises,
    ),
)
