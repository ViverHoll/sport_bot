from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.input import MessageInput, TextInput

from app.services.dialogs.states import NewPost

from .handlers import (
    get_photo_user,
    get_description_user,
    get_tags_user,
    check_tags_in_text,
    get_tags_user_handler,
)

input_text_dialog = Dialog(
    Window(
        Const("Пришлите фотографию поста"),
        MessageInput(
            func=get_photo_user,
            content_types=ContentType.PHOTO,
        ),
        state=NewPost.media,
    ),
    Window(
        Const("Отлично! Пришлите описание своего поста"),
        TextInput(
            id="input_description_post",
            on_success=get_description_user,
        ),
        state=NewPost.description,
    ),
    Window(
        Const(
            "Супер! Пришлите теперь тэги к постам. \n"
            "Если вы выложить пост без тэгов, то просто нажмите на кнопку ниже",
        ),
        TextInput(
            id="input_tags_post",
            type_factory=check_tags_in_text,
            on_success=get_tags_user,
        ),
        SwitchTo(
            text=Const("Пропустить"),
            id="switch_to_skip_tags",
            on_click=get_tags_user_handler,
            state=NewPost.end,
        ),
        state=NewPost.tags,
    ),
    Window(
        Const("Пост успешно опубликован"),
        state=NewPost.end,
    ),
)
