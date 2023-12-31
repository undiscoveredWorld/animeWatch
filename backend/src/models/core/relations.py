from abc import ABC, abstractmethod
from typing import Type

from .crud import ICRUD
from .schemes import Model


class ILinkOnetoManyManager:
    def link(self, one_instance: Model, many_instance: Model):
        pass

    def unlink(self, one_instance: Model):
        pass


class ILinkManyToManyManager:
    def link(self, instance1: Model, instance2: Model):
        pass

    def unlink(self, instance1: Model, instance2: Model):
        pass


class IGetAllLinkedInstances:
    def get_all_instances(self, instance: Model) -> list[Model]:
        pass


class IOneToManyRelationManager(ILinkOnetoManyManager, IGetAllLinkedInstances):
    OneModelCRUD: ICRUD
    ManyModelCRUD: ICRUD


class IManyToManyRelationManager(ILinkManyToManyManager, IGetAllLinkedInstances):
    RelationCrud: Type[ICRUD]


class OneToManyRelationManager(ABC, IOneToManyRelationManager):
    def link(self, one_instance: Model, many_instance: Model):
        self.set_fk_value(one_instance, many_instance.id)
        self.OneModelCRUD.update(one_instance)

    def unlink(self, one_instance: Model):
        self.set_fk_value(one_instance, None)
        self.OneModelCRUD.update(one_instance)

    @abstractmethod
    def get_fk_value(self) -> int | None:
        pass

    @abstractmethod
    def set_fk_value(self, instance: Model, fk_value: int | None) -> None:
        pass
