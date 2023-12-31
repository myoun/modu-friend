from pydantic import BaseModel, Field
from mfriend.ai.schemas import FriendSchema

class LoginSchema(BaseModel):
    id: str = Field(title="사용자 아이디")
    password: str = Field(title="사용자 비밀번호")

class SignupSchema(BaseModel):
    id: str = Field(title="사용자 아이디")
    name: str = Field(title="사용자 이름")
    password: str = Field(title="암호화된 사용자 비밀번호")

class UserSchema(BaseModel):
    id: str = Field(title="사용자 아이디")
    name: str = Field(title="사용자 이름")

    friends: list[FriendSchema] = Field(title="친구들")

    class Config:
        orm_mode = True

class UserAuthSchema(BaseModel):
    id: str = Field()
    salt: str = Field()
    hashed_password: str = Field()

    class Config:
        orm_mode = True

class UserReturnSchema(BaseModel):
    user: UserSchema