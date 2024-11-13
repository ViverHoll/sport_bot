from aiogram import Router

from .dialog import new_admin_dialog


def setup(router: Router) -> None:
    router.include_router(new_admin_dialog)
