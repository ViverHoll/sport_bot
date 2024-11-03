from aiogram import Router

from .dialog import permissions_user_dialog


def setup(router: Router) -> None:
    router.include_router(permissions_user_dialog)
