from fastapi import HTTPException
from mfriend.exceptions import ApplicationError
from typing_extensions import Self

class UserNotFoundError(HTTPException, ApplicationError):

    def __init__(self: Self, user_id: str):
        self.user_id = user_id
        super().__init__(status_code=404, detail=f"Cannot find user `{user_id}`.")

class UserAlreadyExistError(HTTPException, ApplicationError):

    def __init__(self: Self, user_id: str):
        self.user_id = user_id
        super().__init__(status_code=404, detail=f"User `{user_id}` already exists.")

class PasswordIncorrectError(HTTPException, ApplicationError):

    def __init__(self: Self, user_id: str):
        super().__init__(status_code=400, detail=f"Received incorrect password fro user `{user_id}.")
