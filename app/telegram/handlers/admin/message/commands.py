from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.telegram.keyboards.user.reply import get_main_menu

commands_router = Router()


@commands_router.message(F.text == "Главное меню 🔙")
@commands_router.message(CommandStart())
async def admin_command_start(message: Message) -> None:
    await message.answer_sticker(
        sticker="CAACAgIAAxkBAAIE4ma17FQR0nzHkRV729g6KXi6dPhJAAIgAANZu_wlhYqWmghNyX01BA",
    )
    await message.answer(
        "Добро пожаловать",
        reply_markup=get_main_menu(admin=True),
    )
