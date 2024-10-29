from aiogram import F
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Group, Start, SwitchTo, Button
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.options_sportsman.getter import get_info_about_sportsman
from .getters import get_more_foods
from app.dialogs.states import Food, OptionsSportsmanStates, Pay
from .handlers import coming_soon

food_sportsman_dialog = Dialog(
    Window(
        DynamicMedia("sportsman_photo_url"),
        Const("Он много ел, больше всего любил есть курицу с рисом"),
        Group(
            Button(
                text=Const("🍼 Один прием"),
                id="button_one_food",
                on_click=coming_soon
                # state=Food.one_item
            ),
            SwitchTo(
                text=Const("🍱 Весь рацион"),
                id="button_all_food",
                state=Food.more_item
            ),
            Start(
                text=Const("⬅️ Назад"),
                id="button_back",
                state=OptionsSportsmanStates.options
            ),
            width=2
        ),
        state=Food.select,
        getter=get_info_about_sportsman
    ),
    Window(
        Const("Тут какой нибудь рецепт"),
        Start(
            text=Const("💵 Купить подписку"),
            id="button_pay_sub",
            state=Pay.menu,
            when=~F["premium"]
        ),
        # SwitchTo(
        #     text=Const("⬅️ Назад"),
        #     id="button_back",
        #     state=Food.select
        # ),
        Start(
            text=Const("⬅️ Назад"),
            id="button_back",
            state=OptionsSportsmanStates.options
        ),
        state=Food.one_item,
        getter=get_info_about_sportsman
    ),
    Window(
        Format("{food}"),
        # SwitchTo(
        #     text=Const("⬅️ Назад"),
        #     id="button_back",
        #     state=Food.select
        # ),
        Start(
            text=Const("⬅️ Назад"),
            id="button_back",
            state=OptionsSportsmanStates.options
        ),
        state=Food.more_item,
        getter=get_more_foods
    )
)
