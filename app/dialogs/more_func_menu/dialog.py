from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import (
    Button,
    Column,
    Url,
    Row,
    SwitchTo,
    StubScroll,
    Group,
    PrevPage,
    NextPage,
)

from app.dialogs.states import MoreFuncStates

from .getters import get_support_url, paging_sport_food
from .handlers import (
    get_feedback_user,
    get_idea_user,
)

more_func_dialog = Dialog(
    Window(
        Const("Выберите действие:"),
        # Row(
        #     Button(
        #         text=Const("Питание 🍎"),
        #         id="switch_to_food",
        #         on_click=coming_soon
        #         # state=MoreFuncStates.food
        #     ),
        #     SwitchTo(
        #         text=Const("БАДы 🙊"),
        #         id="switch_to_sport_food",
        #         state=MoreFuncStates.sport_food
        #     ),
        # ),
        Column(
            SwitchTo(
                text=Const("Оставить отзыв ✏️"),
                id="button_leave_feedback",
                state=MoreFuncStates.leave_feedback,
            ),
            SwitchTo(
                text=Const("Тех. Поддержка 👨‍💻"),
                id="button_support",
                state=MoreFuncStates.support,
            ),
            SwitchTo(
                text=Const("Предложить идею 🎤"),
                id="button_suggest_idea",
                state=MoreFuncStates.suggest_idea,
            ),
        ),
        state=MoreFuncStates.menu,
    ),
    Window(
        DynamicMedia("photo_sport_food"),
        Const(
            "📄 Название: Протеин\n"
            "🖌 Описание: чистый белок, органическое высокомолекулярное соединение, состоящие из набора аминокислот",
        ),
        StubScroll(
            id="stub_scroll_sport_foods",
            pages="pages",
        ),
        Group(
            Button(
                text=Const("⭐️ Добавить в избранное"),
                id="button_adding_sport_food_in_favorites",
            ),
            width=1,
        ),
        Row(
            PrevPage(
                scroll="stub_scroll_sport_foods",
                text=Const("⬅️"),
            ),
            Button(
                text=Const("✅"),
                id="select_scroll_sport_food",
            ),
            NextPage(
                scroll="stub_scroll_sport_foods",
                text=Const("➡️"),
            ),
        ),
        SwitchTo(
            text=Const("⬅️ Вернуться назад"),
            id="back_to_more_func_menu",
            state=MoreFuncStates.menu,
        ),

        state=MoreFuncStates.sport_food,
        getter=paging_sport_food,
    ),
    Window(
        # Подумать, мб указать фильтр ток на сообщение. Чтобы пользователь не мог присылать любое сообщение в качестве
        # Отзыва
        Const("Введите отзыв:"),
        TextInput(
            id="get_input_feedback_user",
            on_success=get_feedback_user,
        ),
        SwitchTo(
            text=Const("◀️ Назад"),
            id="feedback_button_back",
            state=MoreFuncStates.menu,
        ),
        state=MoreFuncStates.leave_feedback,
    ),
    Window(
        Const("Тут какой-то текст"),
        Url(
            text=Const("Тех. Поддержка"),
            url=Format("{support_url}"),
        ),
        SwitchTo(
            text=Const("◀️ Назад"),
            id="support_button_back",
            state=MoreFuncStates.menu,
        ),
        state=MoreFuncStates.support,
        getter=get_support_url,
    ),
    Window(
        # Подумать, мб указать фильтр ток на сообщение. Чтобы пользователь не мог присылать
        # Любое сообщение в качестве отзыва.
        Const("Введите идею:"),
        TextInput(
            id="get_input_idea_user",
            on_success=get_idea_user,
        ),
        SwitchTo(
            text=Const("◀️ Назад"),
            id="idea_button_back",
            state=MoreFuncStates.menu,
        ),
        state=MoreFuncStates.suggest_idea,
    ),
)
