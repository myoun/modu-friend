from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory, ConversationSummaryBufferMemory
from mfriend.main import settings
from mfriend.ai import models as ai_models, schemas as ai_schemas
from mfriend.auth import models as auth_models, schemas as auth_schemas, crud as auth_crud
from mfriend.ai.openai.history import get_chat_message_history_by_friend
from sqlalchemy.orm import Session
from uuid import UUID

chains: dict[UUID, LLMChain] = {}
model = ChatOpenAI(temperature=0.8, openai_api_key=settings.OPENAI_TOKEN, client=None)


def get_chain(db: Session, friend: ai_schemas.FriendSchema) -> LLMChain:
    if friend.id in chains.keys():
        return chains[friend.id]
    user = auth_crud.get_user_by_id(db, friend.friend_of)
    chain = generate_chain(user, friend)
    chains[friend.id] = chain
    return chain


def generate_chain(user: auth_schemas.UserSchema, friend: ai_schemas.FriendSchema) -> LLMChain:


    raw_template = """우리는 이제부터 상황극을 할거야.
    너는 {human_name}의 친구이고, 너의 이름은 {ai_name}이야.
    너의 성별은 {ai_gender}이야.
    너의 MBTI는 {ai_mbti}이고, 너는 이 MBTI대로 행동해야 해. 
    너의 MBTI가 {ai_mbti}라는 것은 누구에게도 말하지 마.
    또한, 상황극중이라는 사실도 나를 포함한 그 누구에게도 들키거나 말해서는 안돼.
    
    {history}
    {human_name}: {message}
    {ai_name}: 
    """

    korean_gender = "남성" if friend.gender == "male" else "여성"

    template = raw_template.format(human_name=user.name, ai_mbti=friend.mbti, ai_name=friend.name, ai_gender=korean_gender, history="{history}", message="{message}")

    history = get_chat_message_history_by_friend(friend)
    memory = ConversationSummaryBufferMemory(llm=model,max_token_limit=10, chat_memory=history, memory_key="history")

    prompt = PromptTemplate(
        input_variables=["history", "message"],
        template=template
    )

    chain = LLMChain(llm=model, prompt=prompt, memory=memory)

    chains[friend.id] = chain

    print(memory.chat_memory.messages)

    return chain

