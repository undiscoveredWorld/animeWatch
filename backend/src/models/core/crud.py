from .schemes import Model


class ICreate:
    def create(self, instance: Model):
        pass


class IRead:
    def read(self, instance_id: int) -> Model:
        pass

    def read_all(self) -> list[Model]:
        pass


class IUpdate:
    def update(self, instance: Model):
        pass


class IDrop:
    def drop(self, instance: Model):
        pass


class ICRUD(ICreate, IRead, IUpdate, IDrop):
    pass


class CRUDFromList(ICRUD):
    elements: list[Model]

    def __init__(self, elements: list[Model]):
        self.elements = elements

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
