from typing import Any

from aiogram.types import CallbackQuery


async def check_pay(
        callback: CallbackQuery,
        *_: Any
) -> None:
    await callback.answer(
        "Оплата еще не поступила.\n"
        "Проверьте платеж чуть позже.",
        show_alert=True
    )



