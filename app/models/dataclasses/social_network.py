from dataclasses import dataclass
from datetime import datetime


@dataclass
class SocialNetworkType:
    user_id: int
    full_name: str
    age: int
    media: str
    likes: int
    city: str
    description: str
    subscribes: int
    grade: float
    count_posts: int
    created_at: datetime
