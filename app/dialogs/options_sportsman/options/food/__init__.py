from aiogram import Router

from .dialog import food_sportsman_dialog


def setup(router: Router) -> None:
    router.include_router(food_sportsman_dialog)
