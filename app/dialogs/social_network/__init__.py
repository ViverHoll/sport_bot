from aiogram import Router

from . import profile, posts


def setup(router: Router) -> None:
    profile.setup(router)
    posts.setup(router)
