from typing import Any
from pydantic import BaseModel


class MongoBase(BaseModel):
    id: Any

    def model_dump_for_mongo(self) -> dict[str, Any]:
        dump = self.model_dump()

        if "id" in dump and "_id" not in dump:
            dump["_id"] = dump.pop("id")

        return dump
