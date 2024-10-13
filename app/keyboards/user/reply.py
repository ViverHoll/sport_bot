from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def get_main_menu(admin: bool = False) -> ReplyKeyboardMarkup:
    buttons = [
        "Узнать программу 🔥",
        "Профиль 🦁",
        "Соц. сеть 🤩",
        "Другое 🤟",
        "Избранное ⭐️",
        "Подписка 💵",
        "ИИ",
        "Дневник 📕",
        "О боте"
    ]

    keyboard = ReplyKeyboardBuilder()

    for name in buttons:
        keyboard.button(
            text=name
        )

    if admin:
        keyboard.button(
            text="Админ-Панель 🚀"
        )

    keyboard.adjust(1, 2)

    return keyboard.as_markup(
        resize_keyboard=True
    )


def get_social_network_reply_menu() -> ReplyKeyboardMarkup:
    buttons = [
        "Профиль 🎩",
        "Лента ⚡️",
        "Рейтинг 📊",
        "Инструкция 📙",
        "Главное меню 🔙"
    ]
    builder = ReplyKeyboardBuilder()
    for button in buttons:
        builder.button(text=button)

    builder.adjust(2, 1)
    return builder.as_markup(
        resize_keyboard=True
    )
