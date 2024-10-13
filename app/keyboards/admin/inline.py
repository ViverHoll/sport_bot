from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


# создать тут enum, c типами текст и файл и потом через мэджик фильтры их ловить
def get_options_add_sportsman() -> InlineKeyboardMarkup:
    """Функция, которая создает варианты добавления спортсмена."""
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="Текст",
        callback_data="add_sportsman_text"
    )
    keyboard.button(
        text="Файл",
        callback_data="add_sportsman_file"
    )
    keyboard.adjust(1)
    return keyboard.as_markup()
