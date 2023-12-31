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
        one_instance = cls.OneModelCRUD.read(one_instance.id, )
        many_instance = cls.ManyModelCRUD.read(many_instance.id, )

        meta_one_instance: Type
        meta_many_instance: Type

        try:
            meta_one_instance = one_instance.__getattribute__("Meta")
        except AttributeError:
            print("Cannot load metaclass of one instance")

        try:
            meta_many_instance = many_instance.__getattribute__("Meta")
        except AttributeError:
            print("Cannot load metaclass of many instance")

        fks: list[str]
        try:
            fks = meta_one_instance.__getattribute__("FKs")
        except AttributeError:
            print("Cannot load fks of one instance")

        many_instance_name: str
        try:
            many_instance_name = meta_many_instance.__getattribute__("name")
        except AttributeError:
            print("Cannot load name of many instance")

        many_instance_fk: str
        try:
            for fk in fks:
                if many_instance_name in fk:
                    many_instance_fk = fk
                    break
            else:
                print("No fk of many_instance_name not found")
                return

            one_instance.__setattr__(many_instance_fk, many_instance)
        except AttributeError:
            print("FK was found in FKs but not in class")

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


