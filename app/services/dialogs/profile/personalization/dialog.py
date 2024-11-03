from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, SwitchTo, Start

from app.services.dialogs.states import PersonalizationDialog, ProfileDialog

from .handlers import coming_soon
from .windows import (
    main_training_window,
    create_training_program_window,
    ready_training_program_window,
)

personalization_dialog = Dialog(
    Window(
        Const("Здесь мы можете под себя настроить программу и питание!"),
        SwitchTo(
            text=Const("Тренировки 🏋️‍♂️"),
            id="switch_to_personally_training",
            state=PersonalizationDialog.training,
        ),
        Button(
            text=Const("Питание 🥬"),
            id="switch_to_personally_food",
            on_click=coming_soon,
            # state=PersonalizationDialog.food
        ),
        Start(
            text=Const("⬅️"),
            id="start_profile_dialog",
            state=ProfileDialog.menu,
        ),
        state=PersonalizationDialog.options,
    ),
    main_training_window,
    create_training_program_window,
    ready_training_program_window,
)
