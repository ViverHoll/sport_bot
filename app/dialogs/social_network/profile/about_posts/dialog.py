from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, Column, Start

from app.dialogs.social_network.profile.about_posts.handlers import send_user_posts
from app.dialogs.states import (
    AboutPostProfileSocialNetwork,
    NewPost,
    SocialNetworkProfile
)

profile_posts_dialog = Dialog(
    Window(
        Const("Выберите действие"),
        Column(
            Start(
                text=Const("Выложить пост"),
                id="button_post_a_post",
                state=NewPost.media
            ),
            # Button(
            #     text=Const("Удалить пост"),
            #     id="button_delete_post"
            # ),
            Button(
                text=Const("Мои посты"),
                id="button_my_posts",
                on_click=send_user_posts
            ),
            Start(
                text=Const("Назад"),
                id="back_to_profile_social_network_menu",
                state=SocialNetworkProfile.options
            )
        ),
        state=AboutPostProfileSocialNetwork.options
    )
)
