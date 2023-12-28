from models.navigation import NavigationElement


class INavigation:
    @staticmethod
    def get_elements() -> list[NavigationElement]:
        pass


class NavigationFromList(INavigation):
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
