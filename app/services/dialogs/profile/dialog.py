from aiogram import F
from aiogram.enums.content_type import ContentType

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.kbd import (
    Column,
    Start,
    SwitchTo,
    Group,
)

from app.services.dialogs.states import (
    ProfileDialog,
    # PersonalizationDialog,
    SettingProfileUser, PremiumDialog, NewStrengthIndicators, UpdateStrengthIndicator,
)

from .getters import getter
from .handlers import get_new_photo_user

"""
короче я думаю если у пользователя не установлена фотка
то вместо кнопки "изменить фото", выводить "добавить аватарку"
"""
profile_dialog = Dialog(
    Window(
        DynamicMedia(
            "photo_user",
            when=F["photo_user"],
        ),
        # write code for output media user in chat
        # Format(
        #     "<b>🔑 ID:</b> <code>{user_id}</code>\n"
        #     "<b>✨ Подписка:</b> <u>{premium_status}</u>\n"
        #     "<b>🕰 Регистрация:</b> {created_date} (<i>{count_days} дн.</i>)\n"
        #     "<b>⌛️ Осталось:</b> <i>14 дн.</i>\n"
        # ),
        Format(
            "<b>✨ Подписка:</b> <u>{premium_status}</u>\n"
            "<b>Потенциальные gym-bro:</b> <u>{count_gym_bro}</u>\n"
            "<b>Прогресс по параметрам:</b>{parameters}",
        ),
        Column(
            Group(
                Start(
                    text=Const("Обновить параметры"),
                    id="switch_to_update_parameters",
                    state=UpdateStrengthIndicator.update_menu,
                ),
                # SwitchTo(
                #     text=Const("Изменить параметры"),
                #     id="switch_to_edit_parameters",
                #     state=...
                # ),
                # SwitchTo(
                #     text=Const("Точные нынешние параметры"),
                #     id="switch_to_now_parameters",
                #     state=...
                # ),
                Start(
                    text=Const("Добавить параметры"),
                    id="switch_to_add_parameters",
                    state=NewStrengthIndicators.name,
                ),
                width=2,
            ),
            # Start(
            #     text=Const("Персонализация 👨‍💻"),
            #     id="start_personalization",
            #     state=PersonalizationDialog.options
            # ),
            Start(
                text=Const("Настройки ⚙️"),
                id="start_settings_profile_user",
                state=SettingProfileUser.options,
                when=F["premium"],
            ),
            SwitchTo(
                text=Format("{button_photo_name} 📷"),
                id="edit_photo_profile",
                state=ProfileDialog.edit_photo,
                # when=F["photo_user"] is True
            ),
            # SwitchTo(
            #     text=Const("Добавить фото 📷"),
            #     id="edit_photo_profile",
            #     state=ProfileDialog.edit_photo,
            #     when=~F["photo_user"]
            # ),
            Start(
                text=Const("Купить подписку 💵"),
                id="buy_premium",
                state=PremiumDialog.level,
                when=F["premium"],
            ),
        ),
        state=ProfileDialog.menu,
        getter=getter,
    ),
    Window(
        Const("Пришлите новое фото"),
        MessageInput(
            func=get_new_photo_user,
            content_types=ContentType.PHOTO,
        ),
        state=ProfileDialog.edit_photo,
    ),
)
