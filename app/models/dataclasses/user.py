from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class UserType:
    user_id: int
    user_photo: Optional[str]
    username: Optional[str]
    premium: bool
    select_sportsman: bool
    role: str
    created: datetime
    current_sportsman: int
    current_sport_food: int
    current_post: int
    user_photo: Optional[str]
    notifications: Optional[bool]
    notifications_category: Optional[str]  # this enum
    id: int
