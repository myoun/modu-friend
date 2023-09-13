from pydantic import BaseModel, Field
from mfriend.auth.schemas import UserSchema

class FriendPersonalitySchema(BaseModel):
    personality: str
    class Config:
        orm_mode = True

class FriendSchema(BaseModel):
    id: int = Field(title="아이디")
    name: str = Field(title="이름")
    friend_of: str = Field(title="친구 아이디")
    personalities: list['FriendPersonalitySchema'] = Field(title="성격")
    class Config:
        orm_mode = True

class CreateFriendSchema(BaseModel):
    name: str = Field(title="이름")
    friend_of: str = Field(title="친구 아이디")
    personalities: list[str] = Field(title="성격")