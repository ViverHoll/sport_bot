from aiogram import Router

from .dialog import profile_posts_dialog


def setup(router: Router) -> None:
    router.include_router(profile_posts_dialog)
