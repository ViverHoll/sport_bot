from dataclasses import dataclass


@dataclass
class SportFood:
    id: int
    name: str
    description: str
    manual_use: str
    photo: str
