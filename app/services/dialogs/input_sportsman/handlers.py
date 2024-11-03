from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput


async def get_file_handler(
        message: Message,
        _: MessageInput,
        dialog_manager: DialogManager,
) -> None:
    file_name = message.document.file_name
    if file_name.endswith(".txt"):
        await message.answer("Большое спасибо!")
        await dialog_manager.done()
        return
    await message.answer("Вы скинули файл не того формата!")
