from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from app.services.db import HolderDAO
from app.telegram.keyboards.user.inline import get_confirm_edit_photo_menu
from app.state.states import NewProfilePhoto

router = Router()


@router.callback_query(F.data == "edit_photo_profile")
async def editing_photo_in_profile(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.delete()
    await callback.message.answer(
        "Вы можете изменить фото профиля. "
        "Для этого необходимо прислать свое фото."
        "Пришлите то фото, которое хотите видеть у себя в профиле.",
    )
    await state.set_state(NewProfilePhoto.photo)


@router.message(NewProfilePhoto.photo, F.photo)
async def get_new_photo_user(
        message: Message,
        state: FSMContext,
) -> None:
    await state.update_data(
        photo_id=message.photo[-1].file_id,
    )
    await message.answer(
        "Вы уверены что хотите поменять фотографию в профиле?",
        reply_markup=get_confirm_edit_photo_menu(),
    )
    await state.set_state(NewProfilePhoto.confirm)


@router.callback_query(
    NewProfilePhoto.confirm,
    F.data == "confirm_edit_photo",
)
async def confirm_edit_photo(
        callback: CallbackQuery,
        state: FSMContext,
        db: HolderDAO,
) -> None:
    state_data = await state.get_data()
    await db.users.update_user(
        user_id=callback.from_user.id,
        user_photo=state_data["photo_id"],
    )
    await callback.message.edit_text(
        "Фото успешно обновлено",
    )
    await state.clear()


@router.callback_query(
    NewProfilePhoto.confirm,
    F.data == "not_confirm_edit_photo",
)
async def not_confirm_edit_photo(
        callback: CallbackQuery,
        state: FSMContext,
) -> None:
    await callback.message.edit_text(
        "Изменение фотографии успешно отменено",
    )
    await state.clear()


@router.message(NewProfilePhoto.photo)
async def empty_handler(message: Message) -> None:
    await message.answer(
        "Необходимо отправить фотографию",
    )
