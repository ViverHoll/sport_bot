from enum import Enum, IntEnum


class NameSubscribe(Enum):
    """names subscribes."""

    NEWCOMER = "Новичок"
    ADVANCED = "Продвинутый"
    PROFESSIONAL = "Профессионал"


class PriceSubscribe(IntEnum):
    """prices subscribes."""

    NEWCOMER = 399
    ADVANCED = 899
    PROFESSIONAL = 1499
