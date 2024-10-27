from aiogram import F

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format, Const, Multi
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.kbd import (
    NextPage,
    PrevPage,
    Button,
    Group,
    StubScroll
)

from app.dialogs.states import PostSocialNetwork

from .getters import get_posts_with_info

posts_dialog = Dialog(
    Window(
        StubScroll(
            id="scroll_posts",
            pages="pages"
        ),
        DynamicMedia("post_photo"),
        Multi(
            Format(
                "<i>{description}</i>\n\n"
                "{tags}",
                when=F["tags"]
            ),
            Format("<i>{description}</i>",when=~F["tags"])
        ),
        Group(
            Button(
                text=Format("❤️ ({likes})"),
                id="button_heart_post"
            ),
            Button(
                text=Const("✉️"),
                id="button_comment_post"
            ),
            Button(
                text=Const("⭐️"),
                id="button_favourites_post"
            ),
            PrevPage(
                scroll="scroll_posts",
                text=Const("⬅️")
            ),
            NextPage(
                scroll="scroll_posts",
                text=Const("➡️")
            ),
            width=3
        ),
        state=PostSocialNetwork.look_post,
        getter=get_posts_with_info
    )
)
