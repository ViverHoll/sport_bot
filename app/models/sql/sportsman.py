from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel

StrOrAbsent = Annotated[str, mapped_column(
    default="Отсутствует",
    server_default="Отсутствует",
)]


class SportsmanModel(BaseModel):
    __tablename__ = "sportsman"

    name: Mapped[str]
    surname: Mapped[str]
    full_name: Mapped[str]
    description: Mapped[str]

    photo: Mapped[str]
    nickname: Mapped[StrOrAbsent | None]

    exercises: Mapped[StrOrAbsent | None]
    food: Mapped[StrOrAbsent | None]
    music: Mapped[StrOrAbsent | None]
