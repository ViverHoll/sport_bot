from typing import Mapping, Iterable

from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from app.models.config import AppConfig
from app.telegram.callback_factory import SubscribeFactory
from app.telegram.callback_factory.trainer import TrainerCallbackFactory
from app.models.enums.levels_subscribe import (
    NameSubscribe,
    PriceSubscribe,
)
from app.models.enums import SpeciesCoaches


def _create_default_keyboard(
        *,
        buttons: Mapping[str, str],
        adjust: Iterable[int] | None = None,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for text, callback in buttons.items():
        builder.button(
            text=text,
            callback_data=callback,
        )
    if adjust:
        builder.adjust(*adjust)

    return builder.as_markup()


def start_menu() -> InlineKeyboardMarkup:
    buttons = {
        "Персональное ведение": "personalization",
        "Тренировка знаменитостей": "training_popular_people",
        "Фитнес залы": "fitness_room",
        "Магазин": "shop",
        "Соц. сеть": "social_network",
    }
    return _create_default_keyboard(
        buttons=buttons,
        adjust=[2],
    )


def get_coaches_menu() -> InlineKeyboardMarkup:
    buttons = {
        "физ тренер": SpeciesCoaches.PHYSICAL_TRAINER,
        "нутрициолог": SpeciesCoaches.NUTRITIONIST,
        "оздоровитель": SpeciesCoaches.WELLNESS_SPECIALIST,
    }
    builder = InlineKeyboardBuilder()

    for text, trainer in buttons.items():
        builder.button(
            text=text,
            callback_data=TrainerCallbackFactory(
                trainer=trainer,
            ),
        )

    builder.adjust(2)
    return builder.as_markup()


def get_sub_menu(url: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="Подписаться",
        url=url,
    )

    keyboard.button(
        text="Подписался",
        callback_data="check_sub",
    )

    keyboard.adjust(1)
    return keyboard.as_markup()


def pay_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="Оплатить",
        url="https://google.com/",
    )

    keyboard.button(
        text="Оплатил",
        callback_data="check_pay",
    )

    keyboard.adjust(1)
    return keyboard.as_markup()


def get_more_menu() -> InlineKeyboardMarkup:
    buttons = {
        "Оставить отзыв ✏️": "leave_feedback",
        "Тех. Поддержка 👨‍💻": "get_support",
        "Предложить идею 🎤": "suggest_idea",
    }
    return _create_default_keyboard(
        buttons=buttons,
    )


def get_support_menu(config: AppConfig) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="Тех. Поддержка",
        url=config.common.support_url,
    )

    return keyboard.as_markup()


def get_profile_menu(premium: bool = False) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="Изменить фото 📷",
        callback_data="edit_photo_profile",
    )

    if not premium:
        keyboard.button(
            text="Купить подписку 💵",
            callback_data="get_pay_menu",
        )

    keyboard.adjust(1)

    return keyboard.as_markup()


def get_social_network_menu() -> InlineKeyboardMarkup:
    buttons = {
        "Дневник": "diary",
        "Лента": "ribbon",
    }
    return _create_default_keyboard(
        buttons=buttons,
    )


def get_confirm_edit_photo_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Подтверждаю ✅",
        callback_data="confirm_edit_photo",
    )
    builder.button(
        text="Отмена ❌",
        callback_data="not_confirm_edit_photo",
    )
    builder.adjust(1)
    return builder.as_markup()


def get_levels_subscribe() -> InlineKeyboardMarkup:
    buttons = {
        NameSubscribe.NEWCOMER: PriceSubscribe.NEWCOMER,
        NameSubscribe.ADVANCED: PriceSubscribe.ADVANCED,
        NameSubscribe.PROFESSIONAL: PriceSubscribe.PROFESSIONAL,
    }
    builder = InlineKeyboardBuilder()
    for text, callback in buttons.items():
        builder.button(
            text=f"{text.value} ({callback}₽)",
            callback_data=SubscribeFactory(
                name=text,
                price=callback,
            ),
        )
    builder.adjust(1)
    return builder.as_markup()


def get_diary_keyboard() -> InlineKeyboardMarkup:
    buttons = {
        "Силовые": "strength_user",
        "Питание": "food",
    }
    return _create_default_keyboard(
        buttons=buttons,
        adjust=[1],
    )



