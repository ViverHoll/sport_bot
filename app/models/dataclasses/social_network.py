from dataclasses import dataclass
from datetime import datetime


@dataclass
class SocialNetworkType:
    user_id: int
    full_name: str
    age: str
    media: str
    likes: int
    city: str
    description: str
    created_at: datetime
