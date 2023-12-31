from typing import Type

from crud import ICRUD
from schemes import Model


class ILinkOnetoManyManager:
    @classmethod
    def link(cls, one_instance: Model, many_instance: Model):
        pass

    @classmethod
    def unlink(cls, one_instance: Model):
        pass


class IGetAllLinkedInstances:
    @classmethod
    def get_all_instances(cls, instance: Model) -> list[Model]:
        pass


class IGetOtherLinkedInstances:
    @classmethod
    def get_other_linked_instances(cls, instance: Model) -> list[Model]:
        pass


class IOneToManyRelation(ILinkOnetoManyManager, IGetAllLinkedInstances, IGetOtherLinkedInstances):
    OneModelCRUD: Type[ICRUD]
    ManyModelCRUD: Type[ICRUD]
