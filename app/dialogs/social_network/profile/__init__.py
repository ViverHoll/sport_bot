from aiogram import Router

from .dialog import profile_dialog

from . import about_posts


def setup(router: Router) -> None:
    router.include_router(profile_dialog)

    about_posts.setup(router)
