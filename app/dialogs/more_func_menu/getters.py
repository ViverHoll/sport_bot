from typing import Any, TYPE_CHECKING

from aiogram.dispatcher.middlewares.user_context import EventContext
from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from cachetools import TTLCache

if TYPE_CHECKING:
    from app.app_config import AppConfig
    from app.db import HolderDAO

from app.entities.dataclasses import SportFood


async def get_support_url(
        dialog_manager: DialogManager,
        **_: Any
) -> dict[str, Any]:
    config: AppConfig = dialog_manager.middleware_data["config"]

    return {
        "support_url": config.common.support_url
    }


async def paging_sport_food(
        dialog_manager: DialogManager,
        event_context: EventContext,
        ttl_cache: TTLCache,
        **_kwargs
) -> dict[str, Any]:
    db: HolderDAO = dialog_manager.middleware_data["db"]

    if not ttl_cache.get("all_sport_foods", False):
        sport_foods = await db.sport_food.get_all_sport_foods()
        ttl_cache["all_sport_foods"] = sport_foods
    else:
        sport_foods = ttl_cache["all_sport_foods"]

    current_page = await dialog_manager.find("stub_scroll_sport_foods").get_page()

    if f"sportsman_{current_page}" in ttl_cache:
        current_sport_food = SportFood(**ttl_cache.get(f"sport_food_{current_page}"))
    else:
        ttl_cache[f"sport_food_{current_page}"] = sport_foods[current_page].__dict__
        current_sport_food = sport_foods[current_page]

    await db.users.update_user(
        event_context.user_id,
        current_sport_food=current_sport_food.id
    )

    # current_page = await dialog_manager.find("stub_scroll_sport_foods").get_page()

    sport_food_photo = MediaAttachment(
        ContentType.PHOTO,
        file_id=MediaId(
            file_id=current_sport_food.photo
        )
    )

    return {
        "pages": len(sport_foods),
        "current_page": current_page + 1,
        "photo_sport_food": sport_food_photo
    }
