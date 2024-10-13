from aiogram import Router

from .dialog import input_sportsman_dialog


def setup(router: Router) -> None:
    router.include_router(input_sportsman_dialog)
