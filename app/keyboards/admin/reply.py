from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def get_break_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()

    keyboard.button(
        text="Отмена ❌"
    )

    return keyboard.as_markup(
        resize_keyboard=True
    )


def get_admin_menu() -> ReplyKeyboardMarkup:
    buttons = [
        "Добавить спортсмена ➕",
        "Рассылка ✉️",
        "Премиум 💸",  # дать/забрать
        "Забанить ❌",  # пользователя
        "Кол-во юзеров 👌",
        "Главное меню 🔙"
    ]

    keyboard = ReplyKeyboardBuilder()

    for button in buttons:
        keyboard.button(text=button)

    keyboard.adjust(1)
    return keyboard.as_markup(
        resize_keyboard=True
    )
