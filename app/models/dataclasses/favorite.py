from dataclasses import dataclass


@dataclass
class FavoriteType:
    id: int
    user_id: int
    sportsman_id: int | None
