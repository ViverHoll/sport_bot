from dataclasses import dataclass


@dataclass
class LikeType:
    id: int
    user_id: int
    post_id: int
