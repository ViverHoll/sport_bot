from aiogram.fsm.state import State, StatesGroup


class NewSportsman(StatesGroup):
    full_name = State()
    description = State()

    photo_url = State()
    nickname = State()
    mr_olympia = State()
    years_life = State()
    height = State()
    competition_parameters = State()

    exercises = State()
    food = State()
    music = State()


# class InputSportsman(StatesGroup):
#     text = State()
#     file = State()


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


class PersonalizationStates(StatesGroup):
    parameters_user = State()
    select_trainer = State()

