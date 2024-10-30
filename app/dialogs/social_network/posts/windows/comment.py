from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import TextInput

from app.dialogs.states import PostSocialNetwork

from .handlers import get_input_comment

comment_window = Window(
    Const("Введите комментарий"),
    TextInput(
        id="input_comment",
        on_success=get_input_comment,
    ),
    state=PostSocialNetwork.comment,
)
