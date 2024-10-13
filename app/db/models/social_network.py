
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel, TimestampMixin, Int64, Int32, Int16


class SocialNetworkModel(BaseModel, TimestampMixin):
    __tablename__ = "social_network"

    user_id: Mapped[Int64] = mapped_column(
        autoincrement=True,
        primary_key=True
    )
    full_name: Mapped[str]
    age: Mapped[Int16]
    media: Mapped[str]
    likes: Mapped[Int32] = mapped_column(default=0)
    city: Mapped[str]
    description: Mapped[str]

