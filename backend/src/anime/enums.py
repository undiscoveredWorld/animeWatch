from enum import Enum


class TimesOfYear(Enum):
    winter = "Winter"
    spring = "Sprint"
    summer = "Summer"
    autumn = "Autumn"


class AnimeStatus(Enum):
    released = "released"
    previewed = "previewed"
    ongoing = "ongoing"
    dropped = "dropped"
