"""
Stores classes and functions for working with navigation on site

List of classes:
    INavigation -- interface for getting navigation elements
    NavigationFromList -- (testing only) getting navigation from list
"""

from models.schemes.navigation import NavigationElement
from models.database.crud.navigation import get_all_navigation


class INavigation:
    """
    interface for getting navigation elements

    List of methods:
        get_elements -- must get elements from any source and return them in a list
    """
    @classmethod
    def get_elements(cls) -> list[NavigationElement]:
        """
        Method must get elements from any source and return them in a list
        :return: list of navigation elements
        """
        pass


class NavigationFromList(INavigation):
    """
    Testing only. Getting navigation from list
    For working need hardy initialize elements

    List of methods:
        get_elements -- must get elements from any source and return them in a list
    """
    elements: list[str] = ["Ongoings", "OVA", "ONA"]

    @classmethod
    def get_elements(cls) -> list[NavigationElement]:
        result: list[NavigationElement] = list()
        for element in cls.elements:
            result.append(NavigationElement(
                id=0,
                name=element,
                url="/search",
                description=""
            ))
        return result


class NavigationFromSQL(INavigation):

    @classmethod
    def get_elements(cls) -> list[NavigationElement]:
        return get_all_navigation()
    