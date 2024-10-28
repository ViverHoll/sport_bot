from typing import Final

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.db import HolderDAO
from app.keyboards.user.reply import get_social_network_reply_menu
from app.state.states import RegSocialNetwork

router = Router()

_COUNT_ELEMENTS_IN_FULL_NAME: Final[int] = 2


@router.callback_query(F.data == "social_network_registration")
async def start_registration(
        callback: CallbackQuery,
        state: FSMContext
) -> None:
    await callback.message.edit_text(
        "Введите имя и фамилию через пробел. Нужно ввести только буквы\n\n"
        "Например: Вася Пупкин"
    )
    await state.set_state(RegSocialNetwork.full_name)


@router.message(RegSocialNetwork.full_name, F.text)
async def get_full_name_user_handle(
        message: Message,
        state: FSMContext
) -> None:
    full_name = message.text.split()
    if len(full_name) == _COUNT_ELEMENTS_IN_FULL_NAME:
        await state.update_data(full_name=message.text.title())
        await message.answer(
            "Отлично!\n"
            "Теперь введите свой возраст"
        )
        await state.set_state(RegSocialNetwork.age)

    else:
        await message.answer(
            "Нужно ввести только буквы\n\n"
            "Например: Вася Пупкин"
        )


@router.message(RegSocialNetwork.age, F.text)
async def get_age_user_handle(
        message: Message,
        state: FSMContext
) -> None:
    if message.text.isdigit():
        await state.update_data(age=int(message.text))
        await message.answer(
            "Супер!\n"
            "Теперь отправьте свою фотку. Чтобы другие пользователи могли восхищаться вами!"
        )
        await state.set_state(RegSocialNetwork.media)
    else:
        await message.answer(
            "Необходимо отправить цифры!"
        )


@router.message(RegSocialNetwork.media, F.photo)
async def get_photo_user_handle(
        message: Message,
        state: FSMContext
) -> None:
    await state.update_data(media=message.photo[-1].file_id)
    await message.answer(
        "Теперь нужно отправить свою локацию.\n"
        "Введите город:"
    )
    await state.set_state(RegSocialNetwork.city)


@router.message(RegSocialNetwork.media)
async def incorrect_input_user_handle(message: Message) -> None:
    await message.reply("Необходимо отправить фотографию")


@router.message(
    RegSocialNetwork.city,
    F.text
)
async def get_user_location_via_tg_handle(
        message: Message,
        state: FSMContext
) -> None:
    await state.update_data(city=message.text)
    await message.answer(
        "Остался последний шаг.\n"
        "Напишите свое описание, чтобы пользователь мог прочитать его о восхищаться тобой!"
    )
    await state.set_state(RegSocialNetwork.description)


@router.message(RegSocialNetwork.description, F.text)
async def get_description_user_handle(
        message: Message,
        state: FSMContext,
        db: HolderDAO
) -> None:
    state_data = await state.get_data()

    await db.social_network.add_user(
        user_id=message.from_user.id,
        full_name=state_data["full_name"],
        age=state_data["age"],
        media=state_data["media"],
        city=state_data["city"],
        description=message.text
    )
    await message.answer(
        "Регистрация прошла успешно!\n"
        "Приятного пользования",
        reply_markup=get_social_network_reply_menu()
    )
    await state.set_state()
