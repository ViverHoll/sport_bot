from datetime import datetime
from typing import Annotated, TypeAlias
from typing import Any, Final

from sqlalchemy import Function, func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import SmallInteger, Integer, BigInteger, DateTime
from sqlalchemy.orm import registry

Int16: TypeAlias = Annotated[int, 16]
Int32: TypeAlias = Annotated[int, 32]
Int64: TypeAlias = Annotated[int, 64]

NowFunc: Final[Function[Any]] = func.timezone("UTC", func.now())


# @as_declarative()
class BaseModel(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            Int16: SmallInteger,
            Int32: Integer,
            Int64: BigInteger,
            datetime: DateTime(timezone=True),
        },
    )

    id: Mapped[Int64] = mapped_column(
        autoincrement=True,
        primary_key=True,
    )


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        server_default=NowFunc,
    )
