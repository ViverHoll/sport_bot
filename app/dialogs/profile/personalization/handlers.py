from typing import Any

from aiogram.types import CallbackQuery


async def coming_soon(
        callback: CallbackQuery,
        *_args: Any
) -> None:
    await callback.answer(
        "В разработке... 🛠",
        show_alert=True
    )
