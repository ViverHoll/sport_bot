from aiogram import Router

from . import new_admin, new_sportsman


def setup(router: Router) -> None:
    """Setups all dialogs."""
    new_admin.setup(router)
    new_sportsman.setup(router)
