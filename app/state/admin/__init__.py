from aiogram import Router

from .new_sportsman import router as new_sportsman_router

admin_router = Router()
admin_router.include_routers(
    new_sportsman_router,
)
