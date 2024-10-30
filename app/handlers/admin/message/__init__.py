from aiogram import F, Router
from aiogram.filters.magic_data import MagicData

from .commands import commands_router
from .common import router as common_router

message_router = Router()

message_router.message.filter(
    MagicData(F.user.role == "admin"),
)

message_router.include_routers(
    commands_router,
    common_router,
)
