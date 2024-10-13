from aiogram import Router

from .dialog import premium_dialog


def setup(router: Router) -> None:
    router.include_router(premium_dialog)
