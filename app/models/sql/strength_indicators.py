from sqlalchemy.orm import Mapped

from .base import BaseModel, TimestampMixin, Int64


class StrengthIndicatorsModel(BaseModel, TimestampMixin):
    __tablename__ = "strength_indicator"

    # id: Mapped[Int64] = mapped_column(
    #     primary_key=True,
    #     autoincrement=True,
    # )
    user_id: Mapped[Int64]
    name: Mapped[str]
    core: Mapped[str]
