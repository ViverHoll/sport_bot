from typing import Final

from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_dialog import DialogManager

from app.telegram.filters import UserRegSocialNetwork
from app.services.dialogs.states import SocialNetworkProfile, PostSocialNetwork

router = Router()

_REGISTRATION_BUTTON: Final[InlineKeyboardMarkup] = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(
            text="Пройти регистрацию",
            callback_data="social_network_registration",
        ),
    ]],
)

_ALLOWED_TEXTS_SOCIAL_NETWORK: Final[list[str]] = [
    "Профиль 🎩", "Лента ⚡️", "Рейтинг 📊",
]


@router.message(
    UserRegSocialNetwork(),
    F.text == "Профиль 🎩",
)
async def get_profile_user(
        _: Message,
        dialog_manager: DialogManager,
) -> None:
    await dialog_manager.start(
        state=SocialNetworkProfile.options,
    )


@router.message(
    UserRegSocialNetwork(),
    F.text == "Лента ⚡️",
)
async def get_lents_social_network(
        _: Message,
        dialog_manager: DialogManager,
) -> None:
    await dialog_manager.start(
        state=PostSocialNetwork.look_post,
    )


@router.message(
    UserRegSocialNetwork(),
    F.text == "Инструкция 📙",
)
async def get_manual_for_social_network(message: Message) -> None:
    await message.answer(
        "<b><i><u>В разработке...🛠</u></i></b>",
    )


@router.message(
    ~UserRegSocialNetwork(),
    F.text.in_(_ALLOWED_TEXTS_SOCIAL_NETWORK),
)
async def not_reg_user_social_network(message: Message) -> None:
    await message.answer(
        "Необходимо зарегистрироваться",
        reply_markup=_REGISTRATION_BUTTON,
    )
