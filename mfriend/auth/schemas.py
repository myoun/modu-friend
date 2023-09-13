from pydantic import BaseModel, Field

class LoginSchema(BaseModel):
    id: str = Field(title="사용자 아이디")
    hashed_password: str = Field(title="암호화된 사용자 비밀번호")

class SignupSchema(BaseModel):
    id: str = Field(title="사용자 아이디")
    name: str = Field(title="사용자 이름")
    hashed_password: str = Field(title="암호화된 사용자 비밀번호")

class UserSchema(BaseModel):
    id: str = Field(title="사용자 아이디")
    name: str = Field(title="사용자 이름")

    class Config:
        orm_mode = True

class UserReturnSchema(BaseModel):
    user: UserSchema