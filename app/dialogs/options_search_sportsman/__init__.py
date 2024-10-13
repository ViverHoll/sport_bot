from aiogram import Router

from .dialog import options_search_dialog


def setup(router: Router) -> None:
    router.include_router(options_search_dialog)
