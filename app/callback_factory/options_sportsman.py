from aiogram.filters.callback_data import CallbackData


class ExercisesCallbackFactory(CallbackData, prefix="exercises_"):
    sportsman: str


class FoodCallbackFactory(CallbackData, prefix="food_"):
    sportsman: str


class MusicCallbackFactory(CallbackData, prefix="music_"):
    sportsman: str


class InfoOptionsCallbackFactory(CallbackData, prefix="info_"):
    option: str
    sportsman: str
