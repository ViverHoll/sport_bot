from typing import Any

from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select

from app.dialogs.states import PremiumDialog


async def go_to_select_term(
        _: CallbackQuery,
        __: Select,
        manager: DialogManager,
        ___: str,
) -> None:
    await manager.switch_to(
        state=PremiumDialog.term,
    )


async def go_to_buy_menu(
        _: CallbackQuery,
        __: Select,
        manager: DialogManager,
        ___: str,
) -> None:
    await manager.switch_to(
        state=PremiumDialog.buy,
    )


async def check_pay(
        callback: CallbackQuery,
        *_args: Any,
) -> None:
    await callback.answer(
        "Оплата еще не поступила",
        show_alert=True,
    )
