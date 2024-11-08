from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class SportsmanModel(BaseModel):
    __tablename__ = "sportsman"

    sportsmen_id: Mapped[int] = mapped_column(
        autoincrement=True,
    )

    name: Mapped[str]
    surname: Mapped[str]
    full_name: Mapped[str]
    description: Mapped[str]

    photo: Mapped[str]
    nickname: Mapped[str | None]

    exercises: Mapped[str | None]
    food: Mapped[str | None]
    music: Mapped[str | None]
