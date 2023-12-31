from typing import Type

from .crud import ICRUD
from .schemes import Model


class ILinkOnetoManyManager:
    @classmethod
    def link(cls, one_instance: Model, many_instance: Model):
        pass

    @classmethod
    def unlink(cls, one_instance: Model):
        pass


class ILinkManytoManyManager:
    @classmethod
    def link(cls, instance1: Model, instance2: Model):
        pass

    @classmethod
    def unlink(cls, instance1: Model, instance2: Model):
        pass


class IGetAllLinkedInstances:
    @classmethod
    def get_all_instances(cls, instance: Model) -> list[Model]:
        pass


class IOneToManyRelationManager(ILinkOnetoManyManager, IGetAllLinkedInstances):
    OneModelCRUD: Type[ICRUD]
    ManyModelCRUD: Type[ICRUD]


class IManyToManyRelationManager(ILinkManytoManyManager, IGetAllLinkedInstances):
    RelationCrud: Type[ICRUD]


