from .crud import ICRUD
from .crud import CRUDFromList
from .relations import IOneToManyRelationManager
from .relations import OneToManyRelationManager
from .relations import IManyToManyRelationManager


class IData:
    def create_crud(self) -> ICRUD:
        pass

    def create_one_to_many_relation_manager(self) -> IOneToManyRelationManager:
        pass

    def create_many_to_many_relation_manager(self) -> IManyToManyRelationManager:
        pass


class DataFromList(IData):

    def create_crud(self) -> ICRUD:
        return CRUDFromList()

    def create_one_to_many_relation_manager(self) -> IOneToManyRelationManager:
        return OneToManyRelationManager()

    def create_many_to_many_relation_manager(self) -> IManyToManyRelationManager:
        return super().create_many_to_many_relation_manager()
