import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import Select, Url, Button, SwitchTo, Group

from app.dialogs.states import PremiumDialog

from .handlers import go_to_select_term, go_to_buy_menu, check_pay
from .getters import get_subscribes, get_terms

premium_dialog = Dialog(
    Window(
        Const(
            "Есть 3 уровня подписки:\n"
            "<b>- Новичок</b> (399₽)\n"
            "<i><u>Тут описание</u></i>\n\n"
            "<b>- Продвинутый</b> (899₽)\n"
            "<i><u>Тут описание</u></i>\n\n"
            "<b>- Профессионал</b> (1499₽)\n"
            "<i><u>Тут описание</u></i>"
        ),
        Group(
            Select(
                text=Format("{item[0]}"),
                id="select_level_premium",
                item_id_getter=operator.itemgetter(1),
                items="subscribes",
                on_click=go_to_select_term
            ),
            width=1
        ),
        state=PremiumDialog.level,
        getter=get_subscribes
    ),
    Window(
        Const("Выберите срок подписки"),
        Group(
            Select(
                text=Format("{item[0]}"),
                id="select_term_subscribe",
                item_id_getter=operator.itemgetter(1),
                items="terms",
                on_click=go_to_buy_menu
            ),
            width=2
        ),
        SwitchTo(
            text=Const("Назад"),
            id="back_to_main_subscribe_menu",
            state=PremiumDialog.level
        ),
        state=PremiumDialog.term,
        getter=get_terms
    ),
    Window(
        Const("Для оплаты пройдите по ссылке ниже"),
        Url(
            text=Const("Оплатить"),
            url=Const("https://google.com"),
            id="url_for_pay_subscribe",
        ),
        Button(
            text=Const("Проверить оплату"),
            id="check_pay",
            on_click=check_pay
        ),
        state=PremiumDialog.buy
    )
)
