from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from app.services.dialogs.options_sportsman.getter import get_info_about_sportsman
from app.services.dialogs.states import Food, OptionsSportsmanStates, StubScrollSportsman, Exercises, OptionsSearchSportsman

options_sportsman_dialog = Dialog(
    Window(
        DynamicMedia("sportsman_photo_url"),
        Format(
            "<b><i>{sportsman_full_name}</i></b>\n"
            # "<i>{description}</i>\n"
            "🙊 Прозвище: {nickname}\n\n",
            # "🎊 Дата рождения: {years_life}\n\n"
            # "📏 Рост: {height} см\n\n",
        ),
        Start(
            text=Const("🥊 Упражнения"),
            id="button_exercises",
            state=Exercises.more_item,
        ),
        Start(
            text=Const("🥬 Питание"),
            id="button_food",
            state=Food.more_item,
        ),
        # Start(
        #     text=Const("🎧 Музыка"),
        #     id="button_music",
        #     state=Music.select
        # ),
        Start(
            text=Const("⬅️ Назад"),
            id="back_to_select_sportsman",
            # state=StubScrollSportsman.sportsman
            state=StubScrollSportsman.sportsman,
        ),
        state=OptionsSportsmanStates.options,
        getter=get_info_about_sportsman,
    ),

)
"""173"""
"""42"""
