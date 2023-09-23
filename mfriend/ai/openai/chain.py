from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from mfriend.main import settings
from mfriend.ai import models as ai_models
from mfriend.auth import models as auth_models
from mfriend.ai.openai.history import get_chat_message_history_by_friend


def generate_chain(friend: ai_models.Friend) -> LLMChain:

    model = ChatOpenAI(temperature=0.8, openai_api_key=settings.OPENAI_TOKEN)

    template = """우리는 이제부터 연극을 할거야.
    너는 {human_name}의 친구이고, 너의 이름은 {ai_name}이야.
    너의 MBTI는 {ai_mbti}이고, 너는 이 MBTI대로 행동해야 해. 
    너의 MBTI가 {ai_mbti}라는 것은 누구에게도 말하지 마.
    
    {history}
    {ai_name}: 
    """

    prompt = PromptTemplate(
        input_variables=["human_name", "ai_name", "ai_mbti"],
        template=template
    )

    history = get_chat_message_history_by_friend(friend)
    memory = ConversationBufferWindowMemory(k=50000, chat_memory=history)
    chain = LLMChain(llm=model, prompt=prompt, memory=memory)

    return chain

