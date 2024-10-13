from aiogram import F

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import (
    Column,
    Start,
    Button
)

from app.dialogs.states import (
    ProfileDialog,
    PersonalizationDialog,
    SettingProfileUser, PremiumDialog
)

from .getters import getter
from .handlers import coming_soon

"""
короче я думаю если у пользователя не установлена фотка
то вместо кнопки "изменить фото", выводить "добавить аватарку"
"""
profile_dialog = Dialog(
    Window(
        Format(
            "<b>🔑 ID:</b> <code>{user_id}</code>\n"
            "<b>✨ Подписка:</b> <u>{premium_status}</u>\n"
            "<b>🕰 Регистрация:</b> {created_date} (<i>{count_days} дн.</i>)\n"
            "<b>⌛️ Осталось:</b> <i>14 дн.</i>\n"
        ),
        Column(
            Start(
                text=Const("Персонализация 👨‍💻"),
                id="start_personalization",
                state=PersonalizationDialog.options
            ),
            Start(
                text=Const("Настройки ⚙️"),
                id="start_settings_profile_user",
                state=SettingProfileUser.options,
                when=F["premium"]
            ),
            Button(
                text=Const("Изменить фото 📷"),
                id="edit_photo_profile",
                on_click=coming_soon
                # state=ProfileDialog.edit_photo
            ),
            Start(
                text=Const("Купить подписку 💵"),
                id="buy_premium",
                state=PremiumDialog.level,
                when=F["premium"]
            )
        ),
        state=ProfileDialog.menu,
        getter=getter
    )
)
