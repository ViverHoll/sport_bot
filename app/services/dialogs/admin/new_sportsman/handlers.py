from aiogram.types import Message, CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput

from app.services.db import Database
from app.services.dialogs.states import NewSportsmanDialog


async def get_name_sportsman(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        name: str,
) -> None:
    manager.dialog_data["name_sportsman"] = name

    await manager.switch_to(
        state=NewSportsmanDialog.surname,
    )


async def get_surname_sportsman(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        surname: str,
) -> None:
    manager.dialog_data["surname_sportsman"] = surname

    await manager.switch_to(
        state=NewSportsmanDialog.description,
    )


async def get_description_sportsman(
        message: Message,
        widget: ManagedTextInput,
        manager: DialogManager,
        description: str,
) -> None:
    manager.dialog_data["description_sportsman"] = description

    await manager.switch_to(
        state=NewSportsmanDialog.photo,
    )


async def get_photo_sportsman(
        message: Message,
        _: MessageInput,
        manager: DialogManager,
) -> None:
    manager.dialog_data["photo_sportsman"] = message.photo[-1].file_id

    await manager.switch_to(
        state=NewSportsmanDialog.nickname,
    )


async def get_nickname_sportsman(
        message: Message,
        _: ManagedTextInput,
        manager: DialogManager,
        nickname: str,
) -> None:
    manager.dialog_data["nickname"] = nickname

    await manager.switch_to(
        state=NewSportsmanDialog.exercises,
    )


async def get_exercises_sportsman(
        _: Message,
        __: ManagedTextInput,
        manager: DialogManager,
        exercises: str,
) -> None:
    manager.dialog_data["exercises"] = exercises

    await manager.switch_to(
        state=NewSportsmanDialog.food,
    )


async def get_food_sportsman(
        message: Message,
        _: ManagedTextInput,
        manager: DialogManager,
        food_plan: str,
) -> None:
    manager.dialog_data["food"] = food_plan

    await manager.switch_to(
        state=NewSportsmanDialog.music,
    )


# async def get_exercises_sportsman(
#         message: Message,
#         _: MessageInput,
#         manager: DialogManager,
# ) -> None:
#     manager.dialog_data["exercises_sportsman"] = message.text
#
#     await manager.switch_to(
#         state=NewSportsmanDialog.food,
#     )


# async def get_food_sportsman(
#         message: Message,
#         _: MessageInput,
#         manager: DialogManager,
# ) -> None:
#     manager.dialog_data["food_sportsman"] = message.text
#
#     await manager.switch_to(
#         state=NewSportsmanDialog.music,
#     )


async def get_music_sportsman(
        message: Message,
        _: ManagedTextInput,
        manager: DialogManager,
        music: str,
) -> None:
    manager.dialog_data["music"] = music

    await manager.switch_to(
        state=NewSportsmanDialog.confirm,
    )


async def success_confirm_add_new_sportsman(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager,
) -> None:
    db: Database = manager.middleware_data["db"]

    name = manager.dialog_data["name_sportsman"]
    surname = manager.dialog_data["surname_sportsman"]

    get_data = manager.dialog_data.get

    await db.athletes.add_sportsman(
        name=name,
        surname=surname,
        description=manager.dialog_data["description_sportsman"],
        photo=manager.dialog_data["photo_sportsman"],
        nickname=get_data("nickname", "Отсутствует"),
        exercises=get_data("exercises", "Отсутствует"),
        food=get_data("food", "Отсутствует"),
        music=get_data("music", "Отсутствует"),
    )

    await callback.message.answer(
        "Данные о спортсмене успешно добавлены",
    )
    await manager.done()


async def cancel_add_new_sportsman(
        callback: CallbackQuery,
        widget: Button,
        manager: DialogManager,
) -> None:
    await callback.message.answer(
        "Данные о спортсмене не добавлены",
    )
    await manager.done()

