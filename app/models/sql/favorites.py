from sqlalchemy.orm import Mapped, mapped_column

from app.models.enums import FavoritesEnum
from .base import BaseModel, Int64, Int32


class FavoriteModel(BaseModel):
    __tablename__ = "favorites"

    id: Mapped[Int64] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    user_id: Mapped[Int64]
    sportsman_id: Mapped[Int32 | None]
    post_id: Mapped[Int64| None]
    type: Mapped[FavoritesEnum]
