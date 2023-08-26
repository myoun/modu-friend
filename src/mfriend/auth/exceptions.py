from mfriend.exceptions import ApplicationError
from typing_extensions import Self

class UserNotFoundError(ApplicationError):

    def __init__(self: Self, user_id: str):
        self.user_id = user_id
        super().__init__(f"Cannot find user `{user_id}`")


