from aiogram import Router

from .dialog import profile_dialog
from . import personalization, permissions_user


def setup(router: Router) -> None:
    router.include_router(profile_dialog)

    personalization.setup(router)
    permissions_user.setup(router)
