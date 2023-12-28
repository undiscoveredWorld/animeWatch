from typing import Type

from controllers.navigation import INavigation


def get_navigation_context(navigation_source: Type[INavigation]) -> list:
    return navigation_source.get_elements()
