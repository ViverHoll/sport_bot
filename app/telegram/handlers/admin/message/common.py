from aiogram import F, Router
from aiogram.types import Message
from aiogram_dialog import DialogManager

from app.services.dialogs.states import InputSportsman, NewAdminDialog, NewSportsmanDialog
from app.telegram.keyboards.admin.reply import get_admin_menu

router = Router()


@router.message(F.text == "Админ-Панель 🚀")
async def get_admin_menu_handler(message: Message) -> None:
    """Старт админской команды."""
    await message.answer(
        "Вы в админке",
        reply_markup=get_admin_menu(),
    )


@router.message(F.text == "Добавить админа ⚡️")
async def add_admin_handler(
        _: Message,
        dialog_manager: DialogManager
) -> None:
    """Старт диалога добавления админа."""
    await dialog_manager.start(
        state=NewAdminDialog.admin_id
    )


@router.message(F.text == "Добавить спортсмена ➕")
async def add_sportsman_handler(_: Message, dialog_manager: DialogManager) -> None:
    """Старт диалога добавления спортсмена."""
    await dialog_manager.start(
        state=NewSportsmanDialog.name,
    )


# @router.message(F.text == "Рассылка ✉️")
# async def mailing_handle(message: Message) -> None:
#     """Рассылка сообщений."""
#     await message.answer(
#         "Пока нельзя рассылать сообщения",
#     )
#
#
# @router.message(F.text == "Премиум 💸")
# async def get_premium_handle(message: Message) -> None:
#     """Выдача премиума для юзера."""
#     await message.answer(
#         "Пока нельзя ничего делать с премиумом",
#     )
#
#
# @router.message(F.text == "Забанить ❌")
# async def banned_user_handle(message: Message) -> None:
#     """Забанить юзера."""
#     await message.answer(
#         "Пока нельзя никого банить",
#     )


# @router.message(F.text == "Кол-во юзеров 👌")
# async def send_count_users(message: Message) -> None:
#     """Отправка кол-ва юзеров."""
#     await message.answer(
#         "Пока нельзя узнать кол-во юзеров",
#     )
