from typing import Type

from core.crud import ICRUD
from core.crud import crud_from_list
from core.crud import Model
from models.schemes.anime import AnimeShort

GenreWorking = crud_from_list([])
AnimeTagWorking = crud_from_list([])
AnimeCategoryWorking = crud_from_list([])
StudioWorking = crud_from_list([])
SeasonWorking = crud_from_list([])
SeasonOfAnimeWorking = crud_from_list([])
SeriesWorking = crud_from_list([])
AnimeWorking = crud_from_list([])


class IModelsLinkedToAnimeWorking:
    CRUD: Type[ICRUD]

    @classmethod
    def get_linked_to_anime(cls, instance: AnimeShort) -> list[Model]:
        pass


class IAnimeWorking(ICRUD):
    pass
