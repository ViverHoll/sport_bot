from sqlalchemy.orm import Mapped

from .base import BaseModel, Int64, Int32


class FavoriteModel(BaseModel):
    __tablename__ = "favorites"

    user_id: Mapped[Int64]
    sportsman_id: Mapped[Int32 | None]
