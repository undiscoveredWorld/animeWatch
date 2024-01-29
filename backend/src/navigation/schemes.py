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
        from_attributes = True
