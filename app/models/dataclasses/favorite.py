from dataclasses import dataclass

from app.models.enums import FavoritesEnum


@dataclass
class FavoriteType:
    id: int
    user_id: int
    sportsman_id: int | None
    post_id: int | None
    type: FavoritesEnum
