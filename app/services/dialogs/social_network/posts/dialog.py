from aiogram import F

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format, Const, Multi
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.kbd import (
    NextPage,
    PrevPage,
    Group,
    StubScroll,
    SwitchTo, Button,
)

from app.services.dialogs.states import PostSocialNetwork
from .handlers import clicked_like, clicked_favorites_on_post

from .windows import comment_window
from .getters import get_posts_with_info

posts_dialog = Dialog(
    Window(
        StubScroll(
            id="scroll_posts",
            pages="pages",
        ),
        DynamicMedia("post_photo"),
        Multi(
            Format(
                "<i>{description}</i>\n\n"
                "{tags}",
                when=F["tags"],
            ),
            Format(
                "<i>{description}</i>",
                when=~F["tags"],
            ),
        ),
        # SwitchTo(
        #     text=Const("✉️"),
        #     id="button_comment_post",
        #     state=PostSocialNetwork.comment,
        # ),
        Group(
            Button(
                text=Format("{like_heart}"),
                id="button_heart_post",
                on_click=clicked_like,
            ),
            SwitchTo(
                text=Const("✉️"),
                id="button_comment_post",
                state=PostSocialNetwork.comment,
            ),
            Button(
                text=Format("{favorite_stars}"),
                id="button_favourites_post",
                on_click=clicked_favorites_on_post,
            ),
            PrevPage(
                scroll="scroll_posts",
                text=Const("⬅️"),
            ),
            NextPage(
                scroll="scroll_posts",
                text=Const("➡️"),
            ),
            width=3,
        ),
        state=PostSocialNetwork.look_post,
        getter=get_posts_with_info,
    ),
    comment_window,
)
