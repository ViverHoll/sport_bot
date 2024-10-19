from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.keyboards.user.inline import start_menu
from app.keyboards.user.reply import get_main_menu

commands_router = Router()


@commands_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.set_state()
    await message.answer(
        "Добро пожаловать",
        # reply_markup=get_main_menu()
        reply_markup=get_main_menu()
    )
    await message.answer(
        "описание функционала бота",
        reply_markup=start_menu()
    )


@commands_router.message(Command("privacy"))
async def cmd_privacy(message: Message) -> None:
    await message.answer("PRIVACY")
