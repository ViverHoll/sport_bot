from aiogram import Router, F, Bot
# from aiogram.enums import ChatAction
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender

# from app.factory import GptClient
from app.state.states import GptDialog

router = Router()

_BREAK_BUTTON = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Отмена",
                callback_data="break_gpt_dialog"
            )
        ]
    ]
)


@router.message(F.text == "ИИ")
async def start_dialog_with_gpt(message: Message, state: FSMContext) -> None:
    await message.answer("Отправьте свой вопрос")
    await state.set_state(GptDialog.question)


@router.message(GptDialog.question, F.text)
async def answer_question(
        message: Message,
        gpt,
        bot: Bot
) -> None:
    async with ChatActionSender.typing(chat_id=message.from_user.id, bot=bot):
        bot_msg = await message.answer("Генерируем ответ", reply_markup=_BREAK_BUTTON)
        answer_gpt_obj = await gpt.response(
            question=message.text
        )
        answer_gpt = answer_gpt_obj.choices[0].message.content
        await bot_msg.edit_text(
            text=answer_gpt,
            reply_markup=_BREAK_BUTTON
        )
        return


@router.callback_query(GptDialog.question, F.data == "break_gpt_dialog")
async def break_gpt_dialog(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.edit_text("Вы успешно отменили генерацию\n\n"
                                     "*тут переброс в главное меню*")
    await state.clear()
