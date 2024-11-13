from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def get_main_menu(admin: bool = False) -> ReplyKeyboardMarkup:
    # buttons = [
    #     "Узнать программу 🔥",
    #     "Профиль 🦁",
    #     "Соц. сеть 🤩",
    #     "Другое 🤟",
    #     "Избранное ⭐️",
    #     "Подписка 💵",
    #     "ИИ",
    #     "Дневник 📕",
    #     "О боте"
    # ]
    buttons = [
        "Персональное ведение",
        "Тренировка знаменитостей",
        "Фитнес залы",
        "Магазин",
        "Показатели",  # Вместо профиля
        # "Соц. сеть 🤩",
        "Купить подписку 💵",
        "О боте",
        # "Сохраненные спортсмены ⭐️",
    ]

    keyboard = ReplyKeyboardBuilder()

    for name in buttons:
        keyboard.button(
            text=name,
        )

    if admin:
        keyboard.button(
            text="Админ-Панель 🚀",
        )

    keyboard.adjust(2, 2, 2, 1, 1)

    return keyboard.as_markup(
        resize_keyboard=True,
    )


def get_social_network_reply_menu() -> ReplyKeyboardMarkup:
    buttons = [
        "Профиль 🎩",
        "Лента ⚡️",
        # "Рейтинг 📊",
        "Инструкция 📙",
        "Главное меню 🔙",
    ]
    builder = ReplyKeyboardBuilder()
    for button in buttons:
        builder.button(text=button)

    builder.adjust(2, 1)
    return builder.as_markup(
        resize_keyboard=True,
    )


def get_gpt_menu() -> ReplyKeyboardMarkup:
    buttons = [
        "Выбрать тренера",
        "Завершить диалог",
    ]
    builder = ReplyKeyboardBuilder()
    for text in buttons:
        builder.button(text=text)

    builder.adjust(1)
    return builder.as_markup(
        resize_keyboard=True,
    )
