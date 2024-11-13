from typing import Any

from aiogram.dispatcher.middlewares.user_context import EventContext
from aiogram.enums import ContentType
from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.kbd import Button

from cachetools import TTLCache

from app.services.dialogs.states import OptionsSportsmanStates
from app.models.dataclasses import Sportsman, UserType
from app.services.db import Database


async def paging_logic(
        dialog_manager: DialogManager,
        event_context: EventContext,
        ttl_cache: TTLCache,
        db: Database,
        **_kwargs: Any,
) -> dict[str, Any]:
    """Logic scrolling sportsman."""
    if "all_athletes" not in ttl_cache:
        ttl_cache["all_athletes"] = await db.athletes.get_athletes()

    sportsman_list = ttl_cache["all_athletes"]

    current_page = await dialog_manager.find("stub_scroll").get_page()
    current_athlete_key = f"sportsman_{current_page}"

    if current_athlete_key in ttl_cache:
        current_sportsman = Sportsman(
            **ttl_cache[current_athlete_key],
        )
    else:
        current_sportsman = sportsman_list[current_page]
        ttl_cache[f"sportsman_{current_page}"] = current_sportsman.__dict__

    sportsman_photo_url = MediaAttachment(
        ContentType.PHOTO,
        file_id=MediaId(
            file_id=current_sportsman.photo_url,
        ),
    )

    # print(f"{current_sportsman=}")

    await db.users.update_user(
        event_context.user_id,
        current_sportsman=current_sportsman.id,
    )

    return {
        "pages": len(sportsman_list),
        "current_page": current_page + 1,
        "sportsman_photo_url": sportsman_photo_url,
        "bio_sportsman": current_sportsman.description,
        "sportsman_full_name": current_sportsman.full_name,
        # **current_sportsman.__dict__,
    }


async def select_current_sportsman(
        _: CallbackQuery,
        __: Button,
        dialog_manager: DialogManager,
) -> None:
    """Select sportsman."""
    await dialog_manager.done()
    await dialog_manager.start(OptionsSportsmanStates.options)


async def save_in_favorite(
        callback: CallbackQuery,
        __: Button,
        manager: DialogManager,
) -> None:
    """Save sportsman in favorite list."""
    db: Database = manager.middleware_data["db"]
    user: UserType = manager.middleware_data["user"]

    await db.favorite.add_favorite(
        user_id=user.user_id,
        sportsman_id=user.current_sportsman,
    )
    await callback.answer(
        "Спортсмен успешно добавлен!",
    )
