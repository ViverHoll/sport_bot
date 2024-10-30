from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Column, Url
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import Pay

from .getters import get_pay_url
from .handlers import check_pay

pay_dialog = Dialog(
    Window(
        Const("Для оплаты пройдите по ссылке"),
        Column(
            Url(
                text=Const("Перейти к оплате"),
                url=Format("{pay_url}"),
            ),
            Button(
                text=Const("Оплатил"),
                id="button_check_pay",
                on_click=check_pay,
            ),
        ),
        state=Pay.menu,
        getter=get_pay_url,
    ),
    Window(
        Const('Поздравляю вас с приобретением\nТеперь вам доступны функции уровня "Премиум"'),
        state=Pay.success_pay,
    ),
)
