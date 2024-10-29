from typing import Final

from aiogram import Router, F
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from app.callback_factory import SubscribeFactory

from app.models.enums.levels_subscribe import (
    NameSubscribe
)
from app.keyboards.user.inline import get_levels_subscribe

router = Router()

BTN_BACK: Final[InlineKeyboardMarkup] = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(
        text="Назад",
        callback_data="back_to_main_subscribe_menu"
    )]]
)


@router.callback_query(F.data == "back_to_main_subscribe_menu")
async def main_subscribe_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        "Есть 3 уровня подписки:\n"
        "<b>- Новичок</b> (399₽)\n"
        "<i><u>Тут описание</u></i>\n\n"
        "<b>- Продвинутый</b> (899₽)\n"
        "<i><u>Тут описание</u></i>\n\n"
        "<b>- Профессионал</b> (1499₽)\n"
        "<i><u>Тут описание</u></i>",
        reply_markup=get_levels_subscribe()
    )


@router.callback_query(
    SubscribeFactory.filter(F.name == NameSubscribe.NEWCOMER)
)
async def get_info_about_subscribe_newcomer(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        'Информация о тарифе "Новичок"',
        reply_markup=BTN_BACK
    )


@router.callback_query(
    SubscribeFactory.filter(F.name == NameSubscribe.ADVANCED)
)
async def get_info_about_subscribe_advanced(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        'Информация о тарифе "Продвинутый"',
        reply_markup=BTN_BACK
    )


@router.callback_query(
    SubscribeFactory.filter(F.name == NameSubscribe.PROFESSIONAL)
)
async def get_info_about_subscribe_professional(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        'Информация о тарифе "Профессионал"',
        reply_markup=BTN_BACK
    )
