from aiogram import Router

from . import (
    input_sportsman,
    more_func_menu,
    options_search_sportsman,
    options_sportsman,
    pay,
    select_sportsman,
    profile,
    social_network,
    input_post,
    premium,
    strength_indicators
)


def setup_all_dialogs() -> Router:
    """Setting all dialogs."""
    router = Router()

    select_sportsman.setup(router)
    options_sportsman.setup(router)
    more_func_menu.setup(router)
    options_search_sportsman.setup(router)
    pay.setup(router)
    input_sportsman.setup(router)
    profile.setup(router)
    input_post.setup(router)
    premium.setup(router)
    strength_indicators.setup(router)

    social_network.setup(router)

    return router
