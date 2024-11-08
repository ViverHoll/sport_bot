from sqlalchemy.orm import Mapped

from .base import BaseModel, Int64


class GptQueryModel(BaseModel):
    __tablename__ = "gpt_query"

    user_id: Mapped[Int64]
    role: Mapped[str]  # тут сделать енум на 2 роли: assistant, user
    content: Mapped[str]
