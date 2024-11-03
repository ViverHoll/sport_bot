from aiogram import Router

from .dialog import update_strength_indicator_dialog


def setup(router: Router) -> None:
    router.include_router(update_strength_indicator_dialog)
