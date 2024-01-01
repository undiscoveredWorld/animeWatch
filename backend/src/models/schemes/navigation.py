"""
Stores classes and functions for working with navigation data

List of classes:
    NavigationElement -- model for storing information about a navigation element
"""
from .schemes import Model


class NavigationElement(Model):
    """
    Model for storing information about a navigation element

    List of field:
        name -- name of element
        description -- description of element. It will be displayed by hover on element on site
        url -- url where the element leads
    """
    name: str
    description: str | None
    url: str
