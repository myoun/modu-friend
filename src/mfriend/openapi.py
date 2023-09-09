from typing import Any
from enum import Enum

class OpenApiTags(Enum):
    AUTH = "Authentication"
    AI = "AI"

tags_metadata: list[dict[str, Any]] = [
    {
        "name" : "Authentication",
        "description" : "About users"
    },
    {
        "name" : "AI",
        "description" : "Manage Artifial Inteliigences"
    }
]