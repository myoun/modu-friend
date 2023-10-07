from pydantic import BaseModel, Field, validator
from uuid import UUID


class FriendSchema(BaseModel):
    id: UUID = Field(title="아이디")
    name: str = Field(title="이름")
    friend_of: str = Field(title="친구 아이디")
    mbti: str = Field(title="친구 MBTI")
    class Config:
        orm_mode = True

class CreateFriendSchema(BaseModel):
    name: str = Field(title="이름")
    friend_of: str = Field(title="친구 아이디")
    mbti: str = Field(title="친구 MBTI")

    @validator("mbti")
    def mbti_check(cls, v):
        is_mbti = v in ["ENFJ", "ENFP", "ENTJ", "ENTP", "ESFJ", "ESFP", "ESTJ", "ESTP", 
                        "INFJ", "INFP", "INTJ", "INTP", "ISFJ", "ISFP", "ISTJ", "ISTP"]
        if not is_mbti:
            raise ValueError("Invalid MBTI type submitted.")
        return v
class GetFriendSchema(BaseModel):
    friend_id: UUID = Field(title="친구 아이디")    

class GetConversationSchema(BaseModel):
    friend_id: UUID = Field(title="친구 아이디")

class TossMessageSchema(BaseModel):
    friend_id: UUID = Field(title="친구 아이디")
    user_id: str = Field(title="유저 아이디")    
    message: str = Field(title="전달할 메시지")