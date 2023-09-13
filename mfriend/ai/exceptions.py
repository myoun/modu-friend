from fastapi import HTTPException
from mfriend.exceptions import ApplicationError
from typing_extensions import Self

class FriendNotFoundError(HTTPException, ApplicationError):

    def __init__(self: Self, friend_id: int):
        self.friend_id = friend_id
        super().__init__(status_code=404, detail=f"Cannot find friend of id `{friend_id}`.")