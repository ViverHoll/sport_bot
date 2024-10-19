from aiogram.filters.callback_data import CallbackData

from app.entities.enums.trainer import SpeciesCoaches


class TrainerCallbackFactory(CallbackData, prefix="coaches"):
    trainer: SpeciesCoaches
