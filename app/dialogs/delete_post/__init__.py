from aiogram import Router

from .dialog import delete_post_dialog


def setup(router: Router) -> None:
    """Setups dialog."""
    router.include_router(delete_post_dialog)

