from dataclasses import dataclass


@dataclass
class Sportsman:
    # id: int
    name: str
    surname: str
    full_name: str
    description: str
    photo_url: str
    nickname: str
    exercises: dict
    food: str
    music: str
    id: int

