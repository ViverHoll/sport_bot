from aiogram import Router

from .dialog import pay_dialog


def setup(router: Router) -> None:
    router.include_router(pay_dialog)
