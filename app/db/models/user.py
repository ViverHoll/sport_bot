from datetime import datetime

from sqlalchemy import BigInteger, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )

    user_photo: Mapped[str | None]

    username: Mapped[str | None]
    premium: Mapped[bool] = mapped_column(default=False)  # сделать тут енум(куплен, не куплен)

    select_sportsman: Mapped[bool] = mapped_column(
        default=False
    )

    role: Mapped[str] = mapped_column(
        default="user",
        server_default="user"
    )

    created: Mapped[datetime] = mapped_column(
        DateTime(),
        server_default=func.now()
    )

    current_sportsman: Mapped[int | None]
    current_sport_food: Mapped[int | None]
    current_post: Mapped[int | None]

    notifications: Mapped[bool | None] = mapped_column(
        default=True
    )

    # сделать тут енум категориями
    notifications_category: Mapped[str | None]
