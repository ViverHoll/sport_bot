from aiogram import Router

from .dialog import music_sportsman_dialog


def setup(router: Router) -> None:
    router.include_router(music_sportsman_dialog)
