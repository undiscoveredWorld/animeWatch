"""
Support navigation view

List of functions:
    get_navigation_context -- gets navigation context from navigation source and returns it
"""

from typing import Type

from controllers.navigation import INavigation
from models.schemes.navigation import NavigationElement


def get_navigation_context(navigation_source: Type[INavigation]) -> list[NavigationElement]:
    """
    Gets navigation context from navigation source and returns it
    :param navigation_source:
    :return: list of navigation elements
    """
    return navigation_source.get_elements()
