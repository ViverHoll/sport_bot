from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel, Int64


class GptQueryModel(BaseModel):
    __tablename__ = "gpt_query"

    # id: Mapped[Int64] = mapped_column(
    #     primary_key=True,
    #     autoincrement=True,
    # )
    user_id: Mapped[Int64]
    role: Mapped[str]  # тут сделать енум на 2 роли: assistant, user
    content: Mapped[str]
