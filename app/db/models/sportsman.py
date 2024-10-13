from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class SportsmanModel(BaseModel):
    __tablename__ = "sportsman"

    sportsmen_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str]
    surname: Mapped[str]
    description: Mapped[str]

    photo_url: Mapped[str]
    nickname: Mapped[str | None]
    mr_olympia: Mapped[str | None]
    years_life: Mapped[str]
    height: Mapped[int]
    competition_parameters: Mapped[str | None]

    exercises: Mapped[str | None]
    food: Mapped[str | None]
    music: Mapped[str | None]
