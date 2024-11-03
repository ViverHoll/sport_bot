from dataclasses import dataclass


@dataclass
class GptQueryType:
    id: int
    user_id: int
    role: str  # тут сделать енум на 2 роли: assistant, user
    content: str
