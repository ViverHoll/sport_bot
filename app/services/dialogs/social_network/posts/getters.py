from typing import Any, TYPE_CHECKING

from aiogram.dispatcher.middlewares.user_context import EventContext
from aiogram.enums import ContentType

from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId

from cachetools import TTLCache

from app.models.dataclasses import PostType


if TYPE_CHECKING:
    from app.services.db import HolderDAO


async def get_posts_with_info(
        dialog_manager: DialogManager,
        event_context: EventContext,
        ttl_cache: TTLCache,
        **_kwargs: Any,
) -> dict[str, Any]:
    db: HolderDAO = dialog_manager.middleware_data["db"]

    text_like = "❤️" if dialog_manager.dialog_data.get("like") else "🤍"

    if not ttl_cache.get("all_posts", False):
        posts = await db.post.get_all_posts()
        ttl_cache["all_posts"] = posts
    else:
        posts = ttl_cache["all_posts"]

    current_page = await dialog_manager.find("scroll_posts").get_page()
    current_post_cache = ttl_cache.get(f"post_{current_page}", {})
    # current_post = await db.post.get_post_by_id(post_id=user.current_post)

    # current_post = PostType(**current_page_base)

    if current_post_cache:
        current_post = PostType(**current_post_cache)
    else:
        ttl_cache[f"post_{current_page}"] = posts[current_page].__dict__
        current_post = posts[current_page]

    post_photo = MediaAttachment(
        type=ContentType.PHOTO,
        file_id=MediaId(
            file_id=current_post.media,
        ),
    )

    await db.users.update_user(
        event_context.user_id,
        current_post=current_post.post_id,
    )

    return {
        "pages": len(posts),
        "current_page": current_page + 1,
        "post_photo": post_photo,
        "description": current_post.description,
        "tags": current_post.tags,
        "likes": current_post.likes,
        "like_heart": text_like,
        "favorite_stars": dialog_manager.dialog_data.get("favorite_stars", "⭐️"),
    }
