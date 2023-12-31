from typing import Type

from models.core.schemes import Model
from models.schemes.anime import SeasonOfAnime
from models.schemes.anime import Anime
from models.anime import SeasonOfAnimeWorking
from models.anime import AnimeWorking
from models.core.relations import IOneToManyRelation


class AnimeToSeasonRelation(IOneToManyRelation):
    OneModelCRUD = SeasonOfAnimeWorking
    ManyModelCRUD = AnimeWorking

    @classmethod
    def link(cls, one_instance: Model, many_instance: Model):

        cls.OneModelCRUD.update(one_instance)

    @classmethod
    def unlink(cls, one_instance: Model):
        one_instance = cls.OneModelCRUD.read(one_instance.id, )

        one_instance.anime = None

    @classmethod
    def get_all_instances(cls, instance: Anime) -> list[Model]:
        result: list[SeasonOfAnime] = []
        instances: list[SeasonOfAnime] = cls.OneModelCRUD.read_all()

        for i in instances:
            if i.anime == instance:
                result.append(i)

        return result

    @classmethod
    def get_other_linked_instances(cls, instance: Model) -> list[Model]:
        return super().get_other_linked_instances(instance)


