from aiogram import Router

from .dialog import options_sportsman_dialog
from .options import exercises, food, music


def setup(router: Router) -> None:
    router.include_router(options_sportsman_dialog)

    exercises.setup(router)
    food.setup(router)
    music.setup(router)
