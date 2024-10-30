from typing import Iterable, Any


class ArgumentsNotPassedError(Exception):
    def _init__(self, arguments: Iterable[Any]) -> None:
        """Init arguments."""
        self.arguments = arguments

    def __str__(self) -> str:
        return f"Аргументы: {self.arguments} не были переданы."
