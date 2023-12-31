from .schemes import Model
from typing import Type


class ICreate:
    @classmethod
    def create(cls, instance: Model):
        pass


class IRead:
    @classmethod
    def read(cls, instance_id: int) -> Model:
        pass

    @classmethod
    def read_all(cls) -> list[Model]:
        pass


class IUpdate:
    @classmethod
    def update(cls, instance: Model):
        pass


class IDrop:
    @classmethod
    def drop(cls, instance: Model):
        pass


class ICRUD(ICreate, IRead, IUpdate, IDrop):
    pass


class CRUDFromList(ICRUD):
    elements: list[Model]

    @classmethod
    def create(cls, instance: Model):
        cls.elements.append(instance)

    @classmethod
    def read(cls, instance_id: int) -> Model:
        return cls.elements[instance_id]

    @classmethod
    def read_all(cls) -> list[Model]:
        return cls.elements

    @classmethod
    def update(cls, instance: Model):
        for i in range(0, len(cls.elements)):
            if cls.elements[i] == instance:
                cls.elements[i] = instance

    @classmethod
    def drop(cls, instance: Model):
        for element in cls.elements:
            if element.id == instance.id:
                cls.elements.remove(element)


def crud_from_list(elements: list[Model]) -> Type[CRUDFromList]:
    class NewCRUDFromList(CRUDFromList):
        pass

    NewCRUDFromList.elements = elements

    return NewCRUDFromList
