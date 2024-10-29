from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class PostType:
    post_id: int
    post_from_user: int
    media: str
    description: str
    tags: Optional[str]
    likes: int
    created_at: datetime
