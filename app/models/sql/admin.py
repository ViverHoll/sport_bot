from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel, Int64


class AdminModel(BaseModel):
    __tablename__ = "admins"

    admin_id: Mapped[Int64] = mapped_column(
        primary_key=True
    )
    name: Mapped[str]
