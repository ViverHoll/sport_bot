from aiogram import Router

from .dialog import more_func_dialog


def setup(router: Router) -> None:
    router.include_router(more_func_dialog)
