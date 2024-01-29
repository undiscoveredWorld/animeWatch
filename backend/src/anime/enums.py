from enum import Enum


class TimesOfYear(Enum):
    winter = 1
    spring = 2
    summer = 3
    autumn = 4


class AnimeStatus(Enum):
    released = "released"
    previewed = "previewed"
    ongoing = "ongoing"
    dropped = "dropped"
