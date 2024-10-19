from typing import TYPE_CHECKING

from aiogram.types import Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput, ManagedTextInput

from app.dialogs.states import NewPost

if TYPE_CHECKING:

    from app.db import HolderDAO


class NotTagsError(Exception):
    """Ошибка падает когда в слове или тексте не найдено хештегов(#)."""


def check_tags_in_text(text: str) -> str:
    elements = text.split()
    for element in elements:
        if not element.startswith("#"):
            raise NotTagsError
    return text


async def get_photo_user(
        message: Message,
        _: MessageInput,
        manager: DialogManager
) -> None:
    manager.dialog_data["photo_id"] = message.photo[-1].file_id
    # state: FSMContext = manager.middleware_data["state"]
    # await state.update_data(photo_id=message.photo[-1].file_id)
    await manager.switch_to(
        state=NewPost.description
    )


async def get_description_user(
        _: Message,
        __: ManagedTextInput,
        manager: DialogManager,
        text: str
) -> None:
    manager.dialog_data["description"] = text
    # await state.update_data(description=text)

    await manager.switch_to(
        state=NewPost.tags
    )


async def get_tags_user(
        message: Message,
        _: ManagedTextInput,
        manager: DialogManager,
        tags: str
) -> None:
    # print("ya tyt")
    # print(f"{tags=}")
    # manager.dialog_data["tags"] = text
    # state: FSMContext = manager.middleware_data["state"]
    db: HolderDAO = manager.middleware_data["db"]
    await db.post.add_post(
        post_from_user=message.from_user.id,
        media=manager.dialog_data["photo_id"],
        description=manager.dialog_data["description"],
        tags=tags
    )
    # print("yshe tyt")

    # await state.update_data(tags=text)
    await manager.switch_to(
        state=NewPost.end
    )
