from aiogram import Router

from .dialog import scroll_sportsman_dialog


def setup(router: Router) -> None:
    router.include_router(scroll_sportsman_dialog)
