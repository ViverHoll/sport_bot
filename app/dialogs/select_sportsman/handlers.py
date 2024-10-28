from typing import Any, TYPE_CHECKING

from aiogram.dispatcher.middlewares.user_context import EventContext
from aiogram.enums import ContentType
from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import Button

from cachetools import TTLCache

from app.dialogs.states import OptionsSportsmanStates
from app.entities.dataclasses import Sportsman

if TYPE_CHECKING:
    from app.db import HolderDAO


async def paging_logic(
        dialog_manager: DialogManager,
        event_context: EventContext,
        ttl_cache: TTLCache,
        **_kwargs
) -> dict[str, Any]:
    db: HolderDAO = dialog_manager.middleware_data["db"]

    if not ttl_cache.get("all_athletes", False):
        sportsman_list = await db.athletes.get_athletes()
        ttl_cache["all_athletes"] = sportsman_list
    else:
        sportsman_list = ttl_cache["all_athletes"]

    current_page = await dialog_manager.find("stub_scroll").get_page()

    if f"sportsman_{current_page}" in ttl_cache:
        current_sportsman = Sportsman(**ttl_cache.get(f"sportsman_{current_page}"))
    else:
        ttl_cache[f"sportsman_{current_page}"] = sportsman_list[current_page].__dict__
        current_sportsman = sportsman_list[current_page]

    sportsman_photo_url = MediaAttachment(
        ContentType.PHOTO,
        file_id=MediaId(
            file_id=current_sportsman.photo_url
        )
    )

    await db.users.update_user(
        event_context.user_id,
        current_sportsman=current_sportsman.sportsmen_id
    )

    return {
        "pages": len(sportsman_list),
        "current_page": current_page + 1,
        "sportsman_photo_url": sportsman_photo_url,
        "bio_sportsman": current_sportsman.description,
        "sportsman_full_name": f"{current_sportsman.name} {current_sportsman.surname}",
        "competition_parameters": current_sportsman.competition_parameters,
        **current_sportsman.__dict__
    }


async def select_current_sportsman(
        _: CallbackQuery,
        __: Button,
        dialog_manager: DialogManager
) -> None:
    await dialog_manager.done()
    await dialog_manager.start(OptionsSportsmanStates.options)


"""136"""
"""74"""
