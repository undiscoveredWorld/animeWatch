from pydantic import BaseModel


class NavigationElement(BaseModel):
    name: str
    description: str | None
    url: str
