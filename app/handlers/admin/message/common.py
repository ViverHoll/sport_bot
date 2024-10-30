from aiogram import F, Router
from aiogram.types import Message
from aiogram_dialog import DialogManager

from app.dialogs.states import InputSportsman
from app.keyboards.admin.reply import get_admin_menu

router = Router()


@router.message(F.text == "Админ-Панель 🚀")
async def get_admin_menu_handler(message: Message) -> None:
    await message.answer(
        "Вы в админке",
        reply_markup=get_admin_menu(),
    )


@router.message(F.text == "Добавить спортсмена ➕")
async def add_sportsman_handler(_: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(
        state=InputSportsman.select_options,
    )


@router.message(F.text == "Рассылка ✉️")
async def mailing_handle(message: Message) -> None:
    await message.answer(
        "Пока нельзя рассылать сообщения",
    )


@router.message(F.text == "Премиум 💸")
async def get_premium_handle(message: Message) -> None:
    await message.answer(
        "Пока нельзя ничего делать с премиумом",
    )


@router.message(F.text == "Забанить ❌")
async def banned_user_handle(message: Message) -> None:
    await message.answer(
        "Пока нельзя никого банить",
    )


@router.message(F.text == "Кол-во юзеров 👌")
async def send_count_users(message: Message) -> None:
    await message.answer(
        "Пока нельзя узнать кол-во юзеров",
    )
