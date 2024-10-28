from typing import Any, TYPE_CHECKING

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog.widgets.input import ManagedTextInput

from app.dialogs.states import OptionsSportsmanStates

if TYPE_CHECKING:
    from app.db import Database
    from app.entities.dataclasses import UserType


async def search_available(
        callback: CallbackQuery,
        *_: Any
) -> None:
    await callback.answer(
        "Поиск пока недоступен.",
        show_alert=True
    )


# async def get_input_name(
#         message: Message,
#         _: ManagedTextInput,
#         manager: DialogManager,
#         name_sportsman: str
# ) -> None:
#     db: Database =
#     # await message.answer(
#     #     "Данные не найдены. Попробуйте позже"
#     # )
#     # await manager.done()


async def select_sportsman(
        _: CallbackQuery,
        __: Select,
        manager: DialogManager,
        button_id: int
) -> None:
    db: Database = manager.middleware_data["db"]
    user: UserType = manager.middleware_data["user"]
    await db.users.update_user(
        user_id=user.user_id,
        current_sportsman=button_id
    )
    await manager.start(OptionsSportsmanStates.options)
