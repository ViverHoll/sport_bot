from datetime import datetime
from typing import Annotated, TypeAlias
from typing import Any, Final

from sqlalchemy import Function, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import SmallInteger, Integer, BigInteger, DateTime
from sqlalchemy.orm import DeclarativeBase, registry

Int16: TypeAlias = Annotated[int, 16]
Int32: TypeAlias = Annotated[int, 32]
Int64: TypeAlias = Annotated[int, 64]

NowFunc: Final[Function[Any]] = func.timezone("UTC", func.now())


class BaseModel(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            Int16: SmallInteger,
            Int32: Integer,
            Int64: BigInteger,
            datetime: DateTime(timezone=True)
        }
    )


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        server_default=NowFunc
    )
