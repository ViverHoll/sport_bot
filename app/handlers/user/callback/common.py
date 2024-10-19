from aiogram import F, Router
from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager

from app.app_config import AppConfig
from app.dialogs.states import SocialNetworkProfile, OptionsSearchSportsman
from app.keyboards.user.inline import get_support_menu, pay_menu
from app.keyboards.user.reply import get_main_menu

router = Router()


@router.callback_query(F.data == "check_sub")
async def success_check_sub(callback: CallbackQuery) -> None:
    await callback.message.delete()
    await callback.message.answer("Добро пожаловать в бота",
                                  reply_markup=get_main_menu())


@router.callback_query(F.data == "get_pay_menu")
async def answer_pay_menu(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer(
        "Для оплаты пройдите по ссылке",
        reply_markup=pay_menu()
    )


@router.callback_query(F.data == "check_pay")
async def check_pay_menu(callback: CallbackQuery) -> None:
    await callback.answer(
        "Оплата еще не поступила",
        show_alert=True
    )


@router.callback_query(F.data == "strength_user")
async def get_strength_user(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        "Тут силовые по типу:\n\n"
        "<i>Жим лежа</i> - 50кг(50% от с.б.)"
    )


@router.callback_query(F.data == "food")
async def get_food_user(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        "<b><i><u>В разработке...</u></i></b>"
    )


@router.callback_query(F.data == "get_support")
async def inline_get_support(
        callback: CallbackQuery,
        config: AppConfig
) -> None:
    await callback.message.edit_text(
        "Тут какой нибудь текст",
        reply_markup=get_support_menu(config)
    )


@router.callback_query(F.data == "social_network")
async def transition_to_social_network(
        _: CallbackQuery,
        dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(
        state=SocialNetworkProfile.options
    )


@router.callback_query(F.data == "training_popular_people")
async def send_options_search_sportsman(
        _: CallbackQuery,
        dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(
        state=OptionsSearchSportsman.select
    )


@router.callback_query(F.data == "shop")
async def get_shop_menu(callback: CallbackQuery) -> None:
    await callback.answer(
        "В разработке...",
        show_alert=True
    )


@router.callback_query(F.data == "fitness_room")
async def get_fitness_room_menu(callback: CallbackQuery) -> None:
    await callback.answer(
        "В разработке...",
        show_alert=True
    )
