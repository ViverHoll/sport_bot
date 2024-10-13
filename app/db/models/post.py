from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel, Int64, Int32, TimestampMixin


class PostModel(BaseModel, TimestampMixin):
    __tablename__ = "posts"

    post_id: Mapped[Int64] = mapped_column(
        autoincrement=True,
        primary_key=True
    )
    post_from_user: Mapped[Int64]
    media: Mapped[str]
    description: Mapped[str]
    tags: Mapped[str | None]
    likes: Mapped[Int32] = mapped_column(
        default=0
    )
