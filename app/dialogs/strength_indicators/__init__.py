from aiogram import Router

from .dialog import strength_indicators


def setup(router: Router) -> None:
    router.include_router(strength_indicators)
