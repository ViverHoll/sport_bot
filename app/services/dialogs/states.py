from aiogram.fsm.state import State, StatesGroup


class OptionsSearchSportsman(StatesGroup):
    select = State()
    list_sportsman = State()
    sportsman_db = State()
    input_user = State()
    categories = State()
    surname = State()
    name = State()
    exercises = State()
    mr_olympia = State()
    genre_music = State()
    found = State()
    not_found = State()


class StubScrollSportsman(StatesGroup):
    sportsman = State()
    list_sportsman = State()
    sportsman_options = State()


class OptionsSportsmanStates(StatesGroup):
    options = State()
    select_options = State()
    exercises = State()
    food = State()
    music = State()


class MoreFuncStates(StatesGroup):
    menu = State()
    food = State()
    sport_food = State()
    leave_feedback = State()
    thanks_for_feedback = State()
    support = State()
    suggest_idea = State()
    thanks_for_idea = State()


class Exercises(StatesGroup):
    select = State()
    one_item = State()
    more_item = State()
    pay_sub = State()


class Food(StatesGroup):
    select = State()
    one_item = State()
    more_item = State()
    pay_sub = State()


class Music(StatesGroup):
    select = State()
    one_item = State()
    more_item = State()
    pay_sub = State()


class Pay(StatesGroup):
    menu = State()
    success_pay = State()


class InputSportsman(StatesGroup):
    # select_options = State()
    # file = State()
    # text = State()
    name = State()
    surname = State()
    description = State()

    photo = State()
    nickname = State()

    exercises = State()
    food = State()
    music = State()


class SocialNetwork(StatesGroup):
    main_menu = State()
    ribbon = State()
    diary = State()


class ProfileDialog(StatesGroup):
    menu = State()
    notifications = State()
    edit_photo = State()
    buy_premium = State()


class NewStrengthIndicators(StatesGroup):
    start = State()
    name = State()
    core = State()
    confirm = State()


class UpdateStrengthIndicator(StatesGroup):
    update_menu = State()
    select_exercises = State()
    new_core = State()
    confirm = State()


class SocialNetworkProfile(StatesGroup):
    options = State()


class PostSocialNetwork(StatesGroup):
    look_post = State()
    comment = State()
    like = State()


class NewPost(StatesGroup):
    start = State()
    media = State()
    description = State()
    tags = State()
    end = State()


class AboutPostProfileSocialNetwork(StatesGroup):
    options = State()


class PersonalizationDialog(StatesGroup):
    options = State()
    training = State()
    training_program = State()
    ready_training_program = State()
    food = State()


class PremiumDialog(StatesGroup):
    level = State()
    term = State()
    buy = State()


class SettingProfileUser(StatesGroup):
    options = State()
    notifications = State()
    motivation_quotes = State()


class NewSportsmanDialog(StatesGroup):
    name = State()
    surname = State()
    description = State()

    photo = State()
    nickname = State()

    exercises = State()
    food = State()
    music = State()

    confirm = State()


class DeletePostDialog(StatesGroup):
    menu = State()
    confirm = State()


class FavoriteDialog(StatesGroup):
    scroll = State()


class NewAdminDialog(StatesGroup):
    admin_id = State()
    name = State()
    confirm = State()
