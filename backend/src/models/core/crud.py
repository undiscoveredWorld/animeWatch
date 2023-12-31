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

    def create(self, instance: Model):
        self.elements.append(instance)

    def read(self, instance_id: int) -> Model:
        return self.elements[instance_id]

    def read_all(self) -> list[Model]:
        return self.elements

    def update(self, instance: Model):
        for i in range(0, len(self.elements)):
            if self.elements[i] == instance:
                self.elements[i] = instance

    def drop(self, instance: Model):
        for element in self.elements:
            if element.id == instance.id:
                self.elements.remove(element)