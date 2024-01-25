"""
Stores classes and functions for working with navigation data

List of classes:
    NavigationElement -- model for storing information about a navigation element
"""
from pydantic import BaseModel


class NavigationElementBase(BaseModel):
    name: str
    description: str
    url: str


class NavigationElementCreate(NavigationElementBase):
    pass


class NavigationElement(NavigationElementBase):
    id: int

    class Config:
        orm_mode = True
