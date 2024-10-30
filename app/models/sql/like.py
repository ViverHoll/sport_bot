from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel, Int64


class LikeModel(BaseModel):
    __tablename__ = "likes"

    id: Mapped[Int64] = mapped_column(
        autoincrement=True,
        primary_key=True,
    )
    user_id: Mapped[Int64]
    post_id: Mapped[Int64]
    # status: Mapped[bool] = mapped_column(default=True)
