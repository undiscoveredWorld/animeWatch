"""
Stores classes and functions for working with navigation on site

List of classes:
    INavigation -- interface for getting navigation elements
    NavigationFromList -- (testing only) getting navigation from list
"""

from models.navigation import NavigationElement


class INavigation:
    """
    interface for getting navigation elements

    List of methods:
        get_elements -- must get elements from any source and return them in a list
    """
    @staticmethod
    def get_elements() -> list[NavigationElement]:
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

    @staticmethod
    def get_elements() -> list[NavigationElement]:
        result: list[NavigationElement] = list()
        for element in NavigationFromList.elements:
            result.append(NavigationElement(
                name=element,
                url="/search",
                description=""
            ))
        return result
