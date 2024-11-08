from aiogram import Router

from .user import user_router

state_router = Router()
state_router.include_routers(
    user_router,
)
