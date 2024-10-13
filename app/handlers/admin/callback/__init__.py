from aiogram import Router

from .common import router as common_router

callback_router = Router()
callback_router.include_routers(
    common_router
)
