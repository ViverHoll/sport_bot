from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel, TimestampMixin, Int64, Int32


class ProgressModel(BaseModel, TimestampMixin):
    user_id: Mapped[Int64] = mapped_column(
        primary_key=True
    )
    strength: Mapped[str]
