from typing import Final

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender

from sulguk import SULGUK_PARSE_MODE

from app.callback_factory.trainer import TrainerCallbackFactory
from app.keyboards.user.inline import get_coaches_menu
from app.factory.gpt import GptClient
from app.state.states import PersonalizationStates

router = Router()

_BUTTON_BACK: Final[InlineKeyboardMarkup] = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(
            text="Назад",
            callback_data="select_trainer_for_gpt",
        ),
    ]],
)


# @router.callback_query(F.data == "personalization")
@router.message(F.text == "Персональное ведение")
async def start_process_personalization(message: Message, state: FSMContext) -> None:
    await message.answer(
        text="напиши свои цели в фитнесе и нынешние параметры",
    )
    await state.set_state(PersonalizationStates.parameters_user)


@router.message(PersonalizationStates.parameters_user, F.text)
async def get_target_user(message: Message, state: FSMContext) -> None:
    await state.update_data(parameters_user=message.text)
    await message.answer(
        text="спасибо, теперь ты можешь выбрать тренера",
        reply_markup=get_coaches_menu(),
    )
    await state.set_state(PersonalizationStates.select_trainer)


@router.callback_query(F.data == "select_trainer_for_gpt")
async def get_target_for_user_handle(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text="Выберите тренера",
        reply_markup=get_coaches_menu(),
    )


@router.callback_query(
    PersonalizationStates.select_trainer,
    TrainerCallbackFactory.filter(),
)
async def get_select_trainer_user(
        callback: CallbackQuery,
        callback_data: TrainerCallbackFactory,
        bot: Bot,
        state: FSMContext,
        gpt: GptClient,
) -> None:
    # await callback.answer()
    async with ChatActionSender(
            bot=bot,
            chat_id=callback.from_user.id,
            interval=3.0,
    ):
        await callback.message.edit_reply_markup()
        state_data = await state.get_data()

        if callback_data.trainer.value == "physical_trainer":
            more_text = "дай еще программу тренировок под мои требования"
        elif callback_data.trainer.value == "nutritionist":
            more_text = "дай еще план питания под мои требования"
        else:
            more_text = ""
        response_text = (
            f"Привет! подскажи мне: {state_data['parameters_user']}\n\n"
            f"Только ответь как {callback_data.trainer.value}\n\n"
            f"{more_text}\n"
            f"И отправь мне сообщение с html-тэгами"
        )
        gpt_result = await gpt.response(
            question=response_text,
            return_text=True,
        )
        await callback.message.edit_text(
            gpt_result,
            parse_mode=SULGUK_PARSE_MODE,
            reply_markup=_BUTTON_BACK,
        )
