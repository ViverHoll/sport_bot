from typing import TYPE_CHECKING, Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from app.keyboards.user.inline import pay_menu, get_profile_menu

if TYPE_CHECKING:
    from app.models.dataclasses import UserType

# from .func import check_premium


async def select_one_food(
        callback: CallbackQuery,
        *_: Any,
) -> None:
    await callback.message.answer(
        "Куриса с рисом\n\n"
        "Тут рецепт и рекомендации",
        reply_markup=get_profile_menu(),
    )


async def select_all_food(
        callback: CallbackQuery,
        _: Button,
        manager: DialogManager,
) -> None:
    user: UserType = manager.middleware_data["user"]

    if user.premium:
        await callback.message.answer("Тут ссылка на плейлист")
    else:
        await callback.message.answer(
            "Чтобы получить весь плейлист музыки и не только, "
            "Необходимо приобрести подписку\n\n"
            'Чтобы ее оплатить, нажмите на кнопку "оплатить"',
            reply_markup=pay_menu(),
        )
