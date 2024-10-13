from aiogram import Router

from .commands import commands_router
from .common import common_router
from .money_subscribe import router as subscribe_router
from .social_nerwork import router as social_network_router


message_router = Router()
message_router.include_routers(
    commands_router,
    common_router,
    subscribe_router,
    social_network_router
)
