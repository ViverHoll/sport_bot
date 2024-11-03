from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Checkbox, Start

from app.services.dialogs.states import SettingProfileUser, ProfileDialog

from .getters import get_settings_statuses
from .handlers import (
    clicked_on_notifications,
    clicked_on_motivation_quotes,
    clicked_on_show_grade,
    clicked_on_search_gym_bro,
)

permissions_user_dialog = Dialog(
    Window(
        Format(
            "🔔 Уведомления: {notifications_status}\n"
            "⚡️ Мотивационные цитаты: {motivation_status}\n"
            "Показывать оценку: {grade_status}\n"
            "Искать GYM-BRO: {gym_status}",
        ),
        Checkbox(
            checked_text=Const("Отключить ❌"),
            unchecked_text=Const("Включить ✔️"),
            id="checkbox_notifications",
            default=True,
            on_state_changed=clicked_on_notifications,
        ),
        Checkbox(
            checked_text=Const("Отключить ❌"),
            unchecked_text=Const("Включить ✔️"),
            id="checkbox_motivation_quotes",
            default=True,
            on_state_changed=clicked_on_motivation_quotes,
        ),
        Checkbox(
            checked_text=Const("Не показывать ❌"),
            unchecked_text=Const("Показывать ✔️"),
            id="checkbox_show_grade",
            default=True,
            on_state_changed=clicked_on_show_grade,
        ),
        Checkbox(
            checked_text=Const("Не искать ❌"),
            unchecked_text=Const("Искать ✔️"),
            id="checkbox_search_gym_bro",
            default=True,
            on_state_changed=clicked_on_search_gym_bro,
        ),
        Start(
            text=Const("⬅️"),
            id="back_to_profile_dialog_menu",
            state=ProfileDialog.menu,
        ),
        state=SettingProfileUser.options,
        getter=get_settings_statuses,
    ),
)
