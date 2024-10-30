from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.keyboards.admin.reply import get_admin_menu, get_break_menu
from app.state.states import NewSportsman

router = Router()

"""
Сделать так чтобы бот мог ставить реакции к определенным сообщениям
т.е. -> Админ/Юзер пишут какие-то сообщения, бот ставит реакцию какую нибудь, огонь, лайк, какаху.
и тд

Добавить к каждому вводу пример данных
т.е. -> Введите рост и ниже написано: Пример 184



"""


@router.message(F.text == "Добавить спортсмена")
async def start_adding_new_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    await message.answer(
        "Введите имя и фамилию спортсмена",
        reply_markup=get_break_menu(),
    )
    await state.set_state(NewSportsman.full_name)


@router.message(F.text == "Отмена ❌")
async def break_state(
        message: Message,
        state: FSMContext,
) -> None:
    await message.answer(
        "Вы успешно отменили ввод",
        reply_markup=get_admin_menu(),
    )
    await state.clear()


@router.message(NewSportsman.full_name, F.text)
async def get_full_name_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    # мб сделать тут проверку на то, что ввели имя и фамилию, не только имя к примеру
    await state.update_data(full_name=message.text)

    await message.answer(
        "Отлично! Теперь введите описание(биографию) спортсмена",
    )
    await state.set_state(NewSportsman.description)


@router.message(NewSportsman.description, F.text)
async def get_description_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    await state.update_data(description=message.text)

    await message.answer(
        "Введите ссылку на фотку спортсмена",
    )
    await state.set_state(NewSportsman.photo_url)


# Может быть сделать тут проверку на ссылку. Типа то что пользователь действительно ввел юрл,
# не какие-то рандомные символы
@router.message(NewSportsman.photo_url, F.text)
async def get_photo_url_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    await state.update_data(photo_url=message.text)

    await message.answer(
        "Введите кликуху спортсмена. как его называют в народе?",
    )
    await state.set_state(NewSportsman.nickname)


@router.message(NewSportsman.nickname, F.text)
async def get_nickname_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    await state.update_data(nickname=message.text)

    await message.answer(
        "Спортсмен занимал Мистер Олимпию?\n"
        "Если да, то напишите года когда это было.\n"
        'Если нет, то напишите "Не занимал"',
    )
    await state.set_state(NewSportsman.mr_olympia)


# Может сделать тут фильтр на "не занимал". Нужно подумать над этим
@router.message(NewSportsman.mr_olympia, F.text)
async def get_mr_olympia_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    await state.update_data(mr_olympia=message.text)

    await message.answer(
        "Введите годы жизни спортсмена",
    )
    await state.set_state(NewSportsman.years_life)


@router.message(NewSportsman.years_life, F.text)
async def get_years_life_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    await state.update_data(years_life=message.text)

    await message.answer(
        "Введите рост",
    )
    await state.set_state(NewSportsman.height)


# Также мб сделать тут проверку на цифры и рост. Рост не может быть там 300 см
@router.message(NewSportsman.height, F.text)
async def get_height_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    await state.update_data(height=message.text)

    await message.answer(
        "Введите соревновательные данные",
    )
    await state.set_state(NewSportsman.competition_parameters)


@router.message(NewSportsman.competition_parameters, F.text)
async def get_competition_parameters_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    await state.update_data(competition_parameters=message.text)

    await message.answer(
        "Введите упражнения",
    )
    await state.set_state(NewSportsman.exercises)


@router.message(NewSportsman.exercises, F.text)
async def get_exercises_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    await state.update_data(exercises=message.text)

    await message.answer(
        "Введите питание",
    )
    await state.set_state(NewSportsman.food)


@router.message(NewSportsman.food, F.text)
async def get_food_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    await state.update_data(food=message.text)

    await message.answer(
        "Введите музыку",
    )
    await state.set_state(NewSportsman.music)


# Подумать насчет фильтра на файл и на расширение
@router.message(NewSportsman.music, F.text)
async def get_music_sportsman(
        message: Message,
        state: FSMContext,
) -> None:
    """
    Короче:
    1. Подумать над форматом музыки. Как кидать музыку? Плейлистом, файлами, ссылками и тд
    2. Делать после (1) После того как определились форматом, подумать над фильтром. Сделать фильтр под тот формат,
    который выбрали.

    :param message:
    :param state:
    :return:
    """
    await state.update_data(music=message.text)

    # some code ...

    await message.answer(
        "<b>Спортсмен успешно добавлен!</b>",
    )
