from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import SwitchTo

from app.services.dialogs.states import PersonalizationDialog

from .handlers import get_desired_program_training
from .getters import get_gpt_program

main_food_window = Window(
    Const("Персональный план питания"),
    SwitchTo(
        text=Const("Составить план"),
        id="button_create_food_plan",
        state=PersonalizationDialog.training_program,
    ),
    SwitchTo(
        text=Const("Назад"),
        id="switch_to_main_personalization_menu_from_training",
        state=PersonalizationDialog.options,
    ),
    state=PersonalizationDialog.training,
)


create_food_plan_window = Window(
    Const(
        "Введите пожелания по программе или опишите программу которую хотите получить",
    ),
    TextInput(
        id="input_desired_training_program",
        on_success=get_desired_program_training,
    ),
    state=PersonalizationDialog.training_program,
)

ready_food_plan_window = Window(
    Format("{program_training}"),
    SwitchTo(
        text=Const("Назад"),
        id="switch_to_main_training_program_menu",
        state=PersonalizationDialog.training,
    ),
    state=PersonalizationDialog.ready_training_program,
    getter=get_gpt_program,
)





