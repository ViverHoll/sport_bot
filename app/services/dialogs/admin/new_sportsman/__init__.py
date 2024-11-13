from aiogram import Router

from .dialog import new_sportsman_dialog


def setup(router: Router) -> None:
    router.include_router(new_sportsman_dialog)
