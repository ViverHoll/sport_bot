from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.services.db import Database
from app.telegram.keyboards.user.reply import get_main_menu

commands_router = Router()


@commands_router.message(CommandStart())
async def cmd_start(
        message: Message,
        state: FSMContext,
        db: Database,
) -> None:
    """Command start."""

    await state.set_state()
    await message.answer(
        "Добро пожаловать",
        reply_markup=get_main_menu(),
    )


@commands_router.message(Command("privacy"))
async def cmd_privacy(message: Message) -> None:
    """Command privacy."""

    await message.answer("PRIVACY")
