from aiogram.filters.callback_data import CallbackData

from app.models.enums import SpeciesCoaches


class TrainerCallbackFactory(CallbackData, prefix="coaches"):
    trainer: SpeciesCoaches
