from aiogram import F

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.kbd import (
    Button, StubScroll, Row, Start, SwitchTo,
    PrevPage, NextPage,
)

from app.services.dialogs.states import DeletePostDialog, SocialNetworkProfile
from .getters import get_info_post
from .handlers import delete_post_handler

delete_post_dialog = Dialog(
    Window(
        DynamicMedia("post_photo"),
        Format(
            "<i>{description}</i>\n\n"
            "{tags}",
            when=F["tags"],
        ),
        Format(
            "<i>{description}</i>",
            when=~F["tags"],
        ),
        StubScroll(
            id="scroll_delete_post",
            pages="posts",
        ),
        SwitchTo(
            text=Const("Удалить"),
            id="switch_to_delete_post",
            state=DeletePostDialog.confirm,
        ),
        Row(
            PrevPage(
                scroll="scroll_delete_post",
                text=Const("⬅️"),
            ),
            NextPage(
                scroll="scroll_delete_post",
                text=Const("➡️"),
            ),
        ),
        Start(
            text=Const("Назад"),
            id="start_profile_social_network_menu",
            state=SocialNetworkProfile.options,
        ),
        state=DeletePostDialog.menu,
        getter=get_info_post,
    ),
    Window(
        DynamicMedia("post_photo"),
        Format(
            "<i>{description}</i>\n\n"
            "{tags}",
            when=F["tags"],
        ),
        Format(
            "<i>{description}</i>",
            when=~F["tags"],
        ),
        Const("\n\nУдалить пост?"),
        Button(
            text=Const("Удалить"),
            id="button_confirm_delete_post",
            on_click=delete_post_handler,
        ),
        SwitchTo(
            text=Const("Назад"),
            id="back_to_scrolling_posts",
            state=DeletePostDialog.menu,
        ),
        state=DeletePostDialog.confirm,
        getter=get_info_post,
    ),
)
