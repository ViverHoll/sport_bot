from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import ManagedCheckbox


async def clicked_on_notifications(
        _: CallbackQuery,
        checkbox: ManagedCheckbox,
        manager: DialogManager
) -> None:
    manager.dialog_data.update(
        notifications=checkbox.is_checked()
    )


async def clicked_on_motivation_quotes(
        _: CallbackQuery,
        checkbox: ManagedCheckbox,
        manager: DialogManager
) -> None:
    manager.dialog_data.update(
        motivation_quotes=checkbox.is_checked()
    )


async def clicked_on_show_grade(
        _: CallbackQuery,
        checkbox: ManagedCheckbox,
        manager: DialogManager
) -> None:
    manager.dialog_data.update(
        grade=checkbox.is_checked()
    )


async def clicked_on_search_gym_bro(
        _: CallbackQuery,
        checkbox: ManagedCheckbox,
        manager: DialogManager
) -> None:
    manager.dialog_data.update(
        search_gym_bro=checkbox.is_checked()
    )
