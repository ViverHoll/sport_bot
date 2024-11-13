from aiogram import F, Router
from aiogram.filters import CommandStart, or_f
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.telegram.keyboards.user.reply import get_main_menu

commands_router = Router()


@commands_router.message(
    or_f(
        CommandStart(),
        F.text == "Главное меню 🔙",
    ),
)
async def admin_command_start(
        message: Message,
        state: FSMContext,
) -> None:
    """Старт админской команды."""

    await state.set_state()
    await message.answer(
        "Добро пожаловать",
        reply_markup=get_main_menu(admin=True),
    )
