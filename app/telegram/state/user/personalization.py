from typing import Final

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.chat_action import ChatActionSender
from aiogram.fsm.context import FSMContext

from app.telegram.callback_factory.trainer import TrainerCallbackFactory
from app.telegram.keyboards.user.inline import get_coaches_menu
from app.factory.gpt import GptClient
from app.telegram.keyboards.user.reply import get_main_menu, get_gpt_menu
from app.telegram.state.states import GptSteps
from app.services.db import Database

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


@router.message(F.text == "Персональное ведение")
async def start_personalization_user(
        message: Message,
        state: FSMContext,
) -> None:
    """Старт персонализации пользователя."""
    await message.answer("Инструкция", reply_markup=get_gpt_menu())
    await message.answer(
        "Привет! Тут ты можешь задать вопросы по программам, питанию и т.п.",
        reply_markup=NEWBIE_BUTTON,
    )
    await state.set_state(GptSteps.query)


@router.callback_query(
    GptSteps.query,
    F.data == "back_to_main_menu_gpt",
)
async def back_to_main_menu_gpt(
        callback: CallbackQuery,
        state: FSMContext,
) -> None:
    """Возврат в главное меню."""
    await callback.message.edit_text(
        "Привет! Тут ты можешь задать вопросы по программам, питанию и т.п.",
        reply_markup=NEWBIE_BUTTON,
    )
    await state.set_state(GptSteps.query)


@router.callback_query(
    GptSteps.query,
    F.data == "user_newbie",
)
async def get_manual_by_newbie(
        callback: CallbackQuery,
        # state: FSMContext,
) -> None:
    """Получение инструкции для новичка."""
    await callback.message.edit_text(
        "Инструкция для новичка",
        reply_markup=BUTTON_BACK,
    )
    # await state.set_state(GptSteps.newbie)


@router.message(F.text == "Завершить диалог")
async def complete_dialog(
        message: Message,
        state: FSMContext,
        db: Database
) -> None:
    """Завершение диалога с чатом гпт."""
    # clear dialog with gpt in database.
    # await state.set_state()
    await db.gpt.clear_dialog(user_id=message.from_user.id)
    await message.answer(
        "Добро пожаловать",
        reply_markup=get_main_menu(),
    )
    await state.clear()


@router.message(F.text == "Выбрать тренера")
async def select_trainer(
        message: Message,
        state: FSMContext,
) -> None:
    """Выбор тренера."""
    await message.answer(
        "Выберите тренера",
        reply_markup=get_coaches_menu(),
    )
    await state.set_state(GptSteps.options_trainer)


@router.message(
    GptSteps.query,
    F.text,
)
async def get_query_for_gpt(
        message: Message,
        gpt: GptClient,
        bot: Bot,
        db: Database,
) -> None:
    """Отправлению чату гпт сообщение пользователя."""
    async with ChatActionSender(
            bot=bot,
            chat_id=message.from_user.id,
            interval=3.0,
    ):
        gpt_query = await db.gpt.get_all_query(user_id=message.from_user.id)

        if gpt_query:
            query = [
                {
                    "role": q.role,
                    "content": q.content,
                }
                for q in gpt_query
            ]
            query += [
                {
                    "role": "user",
                    "content": (f"{message.text}\n"
                                f"только общайся как человек"),

                },
            ]
            # print(query)
        else:
            query = (f"{message.text}\n"
                     f"только общайся как человек")

        # save query in base.
        # question = (f"{message.text}\n"
        #             f"только общайся как человек")
        gpt_answer = await gpt.response(
            question=query,
            return_text=True,
        )
        await message.answer(
            gpt_answer,
        )
        await db.gpt.add_query(
            user_id=message.from_user.id,
            role="user",
            content=message.text,
        )
        await db.gpt.add_query(
            user_id=message.from_user.id,
            role="assistant",
            content=gpt_answer,
        )


@router.callback_query(
    GptSteps.options_trainer,
    TrainerCallbackFactory.filter(),
)
async def get_select_trainer(
        callback: CallbackQuery,
        callback_data: TrainerCallbackFactory,
        state: FSMContext,
) -> None:
    """Получение выбранного тренера."""
    # save in database.
    await callback.message.edit_text(
        "Тренер успешно выбран.\n"
        "Теперь можете задать ему вопрос.",
    )
    await state.set_state(GptSteps.query)


# @router.message()
async def get_any_type_message(message: Message) -> None:
    """Получение любого типа сообщения."""
    await message.answer(
        "Можно отправить только текст",
    )


"""140"""
