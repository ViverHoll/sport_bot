from aiogram import Router

from .callback import callback_router
from .message import message_router

admin_router = Router()
admin_router.include_routers(
    callback_router,
    message_router
)
