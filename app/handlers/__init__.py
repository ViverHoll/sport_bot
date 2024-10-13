from aiogram import Router

from .admin import admin_router
from .user import user_router

handler_router = Router()
handler_router.include_routers(
    admin_router,
    user_router
)
