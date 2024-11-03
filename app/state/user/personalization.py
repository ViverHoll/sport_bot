from typing import Final

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.chat_action import ChatActionSender


from app.callback_factory.trainer import TrainerCallbackFactory
from app.telegram.keyboards.user.inline import get_coaches_menu
from app.factory.gpt import GptClient
from app.telegram.keyboards.user.reply import get_main_menu

router = Router()

NEWBIE_BUTTON: Final[InlineKeyboardMarkup] = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(
            text="Я новичок",
            callback_data="user_newbie",
        )],
    ],
)

BUTTON_BACK: Final[InlineKeyboardMarkup] = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(
            text="Назад",
            callback_data="back_to_main_menu_gpt",
        ),
    ]],
)


# BUTTON_BACK = Final[InlineKeyboardMarkup] = InlineKeyboardMarkup(
#     inline_keyboard=[[
#         InlineKeyboardButton(
#             text="Назад"
#         )
#     ]]
# )

@router.message(F.text == "Персональное введение")
async def start_personalization_user(message: Message) -> None:
    await message.answer(
        "Привет! Тут ты можешь задать вопросы по программам, питанию и т.п.",
        reply_markup=NEWBIE_BUTTON,
    )


@router.callback_query(F.data == "back_to_main_menu_gpt")
async def back_to_main_menu_gpt(callback: CallbackQuery):
    await callback.message.edit_text(
        "Привет! Тут ты можешь задать вопросы по программам, питанию и т.п.",
        reply_markup=NEWBIE_BUTTON,
    )


@router.callback_query(F.data == "user_newbie")
async def get_manual_by_newbie(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        "Инструкция для новичка",
    )


@router.message(F.text)
async def get_query_for_gpt(
        message: Message,
        gpt: GptClient,
        bot: Bot,
) -> None:
    async with ChatActionSender(
            bot=bot,
            chat_id=message.from_user.id,
            interval=3.0,
    ):
        question = (f"{message.text}\n"
                    f"только общайся как человек")
        gpt_answer = await gpt.response(
            question=question,
            return_text=True,
        )
        await message.answer(
            gpt_answer,
        )


@router.message(F.text == "Завершить диалог")
async def complete_dialog(message: Message):
    # clear dialog with gpt in database.
    # await state.set_state()
    await message.answer(
        "Добро пожаловать",
        reply_markup=get_main_menu(),
    )


@router.message(F.text == "Выбрать тренера")
async def select_trainer(message: Message):
    await message.answer(
        "Выберите тренера",
        reply_markup=get_coaches_menu(),
    )


@router.callback_query(TrainerCallbackFactory.filter())
async def get_select_trainer(
        callback: CallbackQuery,
        callback_data: TrainerCallbackFactory,
) -> None:
    # save in database.
    await callback.message.edit_text(
        "Тренер успешно выбран.\n"
        "Теперь можете задать ему вопрос.",
    )


@router.message()
async def get_any_type_message(message: Message):
    await message.answer(
        "Можно отправить только текст",
    )
