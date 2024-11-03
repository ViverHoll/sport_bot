from aiogram import Router


from .dialog import exercises_sportsman_dialog


def setup(router: Router) -> None:
    router.include_router(exercises_sportsman_dialog)

