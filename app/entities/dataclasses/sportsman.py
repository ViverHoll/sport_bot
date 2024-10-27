from dataclasses import dataclass


@dataclass
class Sportsman:
    sportsmen_id: int

    name: str
    surname: str
    description: str

    photo_url: str
    nickname: str
    mr_olympia: str
    years_life: str
    height: int
    competition_parameters: str

    exercises: dict
    food: str
    music: str

    def full_name(self) -> str:
        return f"{self.name} {self.surname}".title()
