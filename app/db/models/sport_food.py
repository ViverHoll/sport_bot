from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class SportFoodModel(BaseModel):
    __tablename__ = "sport_foods"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    manual_use: Mapped[str]
    photo: Mapped[str]
