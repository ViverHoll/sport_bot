from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.media import DynamicMedia

from app.dialogs.states import (SocialNetworkProfile,
                                AboutPostProfileSocialNetwork)
from .getters import get_data_user

profile_dialog = Dialog(
    Window(
        DynamicMedia("media", when="media"),
        Format(
            "Имя Фамилия: <b><i>{full_name}</i></b>\n"
            "Возраст: <b>{age}</b>\n"
            "Описание: <i>{description}</i>\n"
            "Город: <u>{city}</u>\n"
            "Всего лайков: <s>{likes}</s>"
        ),
        # Button(
        #     text=Const("Прогресс"),
        #     id="button_progress"
        # ),
        Start(
            text=Const("Посты"),
            id="button_about_posts",
            state=AboutPostProfileSocialNetwork.options
        ),
        state=SocialNetworkProfile.options,
        getter=get_data_user
    )
)
