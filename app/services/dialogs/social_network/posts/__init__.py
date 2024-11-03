from aiogram import Router

from .dialog import posts_dialog


def setup(router: Router) -> None:
    router.include_router(posts_dialog)
