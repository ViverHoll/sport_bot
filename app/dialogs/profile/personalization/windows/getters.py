from typing import Any

from aiogram_dialog import DialogManager


async def get_gpt_program(
        dialog_manager: DialogManager,
        **_kwargs: Any
) -> dict[str, str]:
    # gpt_program: str = dialog_manager.dialog_data["gpt_program"]
    return {
        "program_training": dialog_manager.dialog_data["gpt_program"]
    }

