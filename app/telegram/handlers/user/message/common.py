import logging

from aiogram import F, Router, Bot
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from app.services.db import Database
from app.models.config import AppConfig
from app.services.dialogs.states import MoreFuncStates, OptionsSearchSportsman, ProfileDialog, PremiumDialog
# from app.factory import GptClient
from app.telegram.keyboards.user.inline import get_diary_keyboard

# if TYPE_CHECKING:
#     from app.factory import GptClient

common_router = Router()
logger = logging.getLogger()


# @common_router.message()
# async def go_gpt(message: Message, gpt) -> None:
#     await message.answer("wait pls...")
#     answer = await gpt.response(message.text)
#     await message.answer(f"{answer}")
#     await message.answer_photo()


@common_router.message(F.text == "Тренировка знаменитостей")
async def go_sportsmen_menu(
        _: Message,
        dialog_manager: DialogManager,
) -> None:
    await dialog_manager.start(
        state=OptionsSearchSportsman.select,
        mode=StartMode.RESET_STACK,
    )


@common_router.message(F.text == "Дневник 📕")
async def get_diary_user(message: Message) -> None:
    await message.answer(
        "Тут мб фотка",
    )
    await message.answer(
        "Тут твой дневник",
        reply_markup=get_diary_keyboard(),
    )


@common_router.message(F.text == "О боте")
async def get_info_about_bot(
        _: Message,
        dialog_manager: DialogManager,
) -> None:
    # await message.answer(
    #     "<b><i><u>В разработке...</u></i></b>"
    # )
    await dialog_manager.start(
        state=MoreFuncStates.menu,
    )


@common_router.message(F.text == "Показатели")
async def get_profile_user(
        _: Message,
        dialog_manager: DialogManager,
) -> None:
    await dialog_manager.start(state=ProfileDialog.menu)


@common_router.message(F.text == "Тех. Поддержка 👨‍💻")
async def get_contact_support(message: Message, config: AppConfig) -> None:
    await message.answer(
        f"Ссылка не тех поддержку: {config.common.support_url}",
    )


@common_router.message(F.text == "Другое 🤟")
async def get_more_func_handler(
        _: Message,
        dialog_manager: DialogManager,
) -> None:
    await dialog_manager.start(MoreFuncStates.menu)


@common_router.message(F.text == "Сохраненные спортсмены ⭐️")
async def get_favorites_user(
        message: Message,
        db: Database,
        bot: Bot,
) -> None:
    # await message.answer(
    #     "<b><i><u>В разработке...🛠</u></i></b>",
    # )
    favorites = await db.favorite.get_all_favorites(
        user_id=message.from_user.id,
    )

    for favorite in favorites:
        sportsman = await db.athletes.get_sportsman_by_id(
            sportsman_id=favorite.sportsman_id,
        )
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"{sportsman}",
        )


    await message.answer("все...")


# @common_router.message(F.text == "Соц. сеть 🤩")
# async def open_our_social_network(message: Message) -> None:
#     await message.answer(
#         "Добро пожаловать в нашу социальную сеть!\n\n"
#         "Здесь ты можешь делиться своими результатами, смотреть результаты других, ставить оценки и многое другое!",
#         reply_markup=get_social_network_reply_menu(),
#     )


# @common_router.message(F.text == "Главное меню 🔙")
# async def back_to_main_menu(message: Message) -> None:
#     await message.answer(
#         "Главное меню",
#         reply_markup=get_main_menu(),
#     )


@common_router.message(F.text == "Магазин")
async def get_market(message: Message) -> None:
    await message.answer(
        "<b><i><u>В разработке...</u></i></b>",
    )


@common_router.message(F.text == "Фитнес залы")
async def get_fitness_gym(message: Message) -> None:
    await message.answer(
        "<b><i><u>В разработке...</u></i></b>",
    )


# @common_router.message(F.text == "Инструкция 📙")
# async def get_manual(message: Message) -> None:
#     await message.answer(
#         "<b><i><u>В разработке...</u></i></b>",
#     )


@common_router.message(F.text == "Купить подписку 💵")
async def get_info_about_subscribe(
        _: Message,
        dialog_manager: DialogManager,
) -> None:
    await dialog_manager.start(
        state=PremiumDialog.level,
        mode=StartMode.RESET_STACK,
    )


# @common_router.message(F.sticker)
# async def send_sticker_id(message: Message) -> None:
#     await message.answer(
#         f"{message.sticker.file_id}",
#     )
#
#
# @common_router.message(F.video)
# async def send_video_id(message: Message) -> None:
#     await message.answer(
#         f"{message.video.file_id}",
#     )
#
#
@common_router.message(F.photo)
async def send_photo_id(message: Message) -> None:
    await message.answer(
        f"{message.photo[-1].file_id}",
    )
