from aiogram import Router

from .edit_photo import router as edit_photo_router
from .social_network_registration import router as social_network_reg_router
from .gpt import router as gpt_router

user_router = Router()
user_router.include_routers(
    social_network_reg_router,
    edit_photo_router,
    gpt_router
)
