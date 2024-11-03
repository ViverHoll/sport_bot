from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender

from app.services.dialogs.states import PersonalizationDialog

if TYPE_CHECKING:
    from aiogram import Bot

    from app.factory import GptClient


async def get_desired_program_training(
        message: Message,
        _: ManagedTextInput,
        manager: DialogManager,
        __: str,
) -> None:
    gpt: GptClient = manager.middleware_data["gpt"]
    bot: Bot = manager.middleware_data["bot"]

    async with ChatActionSender.typing(
            chat_id=message.from_user.id,
            bot=bot,
            interval=3.0,
    ):
        answer_gpt = await gpt.response(
            question=message.text,
            return_text=True,
        )
        manager.dialog_data["gpt_program"] = answer_gpt
        await manager.switch_to(
            state=PersonalizationDialog.ready_training_program,
        )



