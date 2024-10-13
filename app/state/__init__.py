from aiogram import Router

from .admin import admin_router
from .user import user_router

state_router = Router()
state_router.include_routers(
    admin_router,
    user_router
)
