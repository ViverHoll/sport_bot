from aiogram import Router

from app.telegram.filters import AdminFilter

from .callback import callback_router
from .message import message_router

admin_router = Router()

admin_router.message(AdminFilter())
admin_router.callback_query(AdminFilter())

admin_router.include_routers(
    callback_router,
    message_router,
)
