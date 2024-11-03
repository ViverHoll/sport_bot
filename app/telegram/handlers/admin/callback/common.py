from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from app.services.dialogs.states import InputSportsman

router = Router()


@router.callback_query(F.data == "add_sportsman_file")
async def start_add_sportsman_dialog(
        _: CallbackQuery,
        dialog_manager: DialogManager,
) -> None:
    await dialog_manager.start(InputSportsman.select_options)
