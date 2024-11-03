from aiogram import Router

from .dialog import personalization_dialog


def setup(router: Router) -> None:
    router.include_router(personalization_dialog)
