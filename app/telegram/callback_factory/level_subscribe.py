from aiogram.filters.callback_data import CallbackData

from app.models.enums.levels_subscribe import (
    NameSubscribe,
    PriceSubscribe,
)


class SubscribeFactory(CallbackData, prefix="buy"):
    name: NameSubscribe
    price: PriceSubscribe
