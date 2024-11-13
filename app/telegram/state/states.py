from aiogram.fsm.state import State, StatesGroup


class NewProfilePhoto(StatesGroup):
    photo = State()
    confirm = State()


class RegSocialNetwork(StatesGroup):
    full_name = State()
    age = State()
    media = State()
    city = State()
    description = State()


class GptDialog(StatesGroup):
    question = State()


class GptSteps(StatesGroup):
    start = State()
    select_trainer = State()
    query = State()
    newbie = State()
    end_dialog = State()
    options_trainer = State()


class NewAdmin(StatesGroup):
    admin_id = State()
    name = State()
    confirm = State()
