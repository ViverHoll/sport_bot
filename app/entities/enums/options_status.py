from enum import Enum


class PremiumStatusEnum(Enum):
    PURCHASED = "Куплена"
    NOT_PURCHASED = "Не куплена"


class NotificationsStatusEnum(Enum):
    ON = "Включены"
    OFF = "Выключены"
