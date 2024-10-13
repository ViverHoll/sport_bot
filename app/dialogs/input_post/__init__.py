from aiogram import Router

from .dialog import input_text_dialog


def setup(router: Router) -> None:
    router.include_router(input_text_dialog)
