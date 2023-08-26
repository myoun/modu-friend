from typing import Any
from enum import Enum

class OpenApiTags(Enum):
    AUTH = "Authentication"

tags_metadata: list[dict[str, Any]] = [
    {
        "name" : "Authentication",
        "description" : "About users"
    }
]