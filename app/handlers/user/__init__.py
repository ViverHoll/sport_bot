from aiogram import Router

from .callback import callback_router
from .message import message_router

user_router = Router()
user_router.include_routers(
    callback_router,
    message_router,
)
