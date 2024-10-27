import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import (
    SwitchTo, Start,
    PrevPage, CurrentPage, NextPage,
    Select, Column, Row
)

from app.dialogs.states import UpdateStrengthIndicator, ProfileDialog
from app.dialogs.strength_indicators.update.getters import get_all_exercises, get_exercise_info, get_data
from app.dialogs.strength_indicators.update.handlers import get_select_exercise, get_new_input_strength_indicator, \
    update_strength_indicator

update_strength_indicator_dialog = Dialog(
    Window(
        Const("Выберите упражнение:"),
        # List(
        #     field=Format(
        #         ""
        #     )
        # ),
        Column(
            Select(
                text=Format("{item[0]}"),
                id="select_exercise_for_update",
                item_id_getter=operator.itemgetter(1),
                items="exercises",
                on_click=get_select_exercise,
                type_factory=int
            ),
        ),
        # Row(
        #     PrevPage(
        #         scroll="scroll_list_sportsman",
        #         text=Const("⬅️")
        #     ),
        #     CurrentPage(
        #         scroll="scroll_list_sportsman"
        #     ),
        #     NextPage(
        #         scroll="scroll_list_sportsman",
        #         text=Const("➡️")
        #     )
        # ),
        Start(
            text=Const("Назад"),
            id="switch_to_options_search_menu",
            state=ProfileDialog.menu
        ),
        state=UpdateStrengthIndicator.update_menu,
        getter=get_all_exercises
    ),
    Window(
        Format("{exercise_info}\n\nВведите новые силовые"),
        TextInput(
            id="input_new_strength_indicator",
            on_success=get_new_input_strength_indicator
        ),
        state=UpdateStrengthIndicator.new_core,
        getter=get_exercise_info
    ),
    Window(
        Format(
            "Было:\n"
            "{old_exercise_info}\n\n"
            "Стало:\n"
            "{new_exercise_info}\n\n"
            "Вы подтверждаете изменение?"
        ),
        Start(
            text=Const("Подтверждаю"),
            id="confirm_update_strength_indicator",
            on_click=update_strength_indicator,
            state=ProfileDialog.menu
        ),
        Start(
            text=Const("Отмена"),
            id="not_confirm_strength_indicator",
            state=ProfileDialog.menu,
        ),
        state=UpdateStrengthIndicator.confirm,
        getter=get_data
    )
)
