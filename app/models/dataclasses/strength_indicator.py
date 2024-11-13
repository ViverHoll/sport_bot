from dataclasses import dataclass
from datetime import datetime


@dataclass
class StrengthIndicatorType:
    # id: int
    user_id: int
    name: str
    core: str
    id: int
    created_at: datetime