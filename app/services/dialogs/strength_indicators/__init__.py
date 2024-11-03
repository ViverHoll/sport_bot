from aiogram import Router

from .dialog import strength_indicators

from . import update


def setup(router: Router) -> None:
    router.include_router(strength_indicators)

    update.setup(router)
