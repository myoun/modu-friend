from langchain import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.memory import ConversationBufferWindowMemory

conversations: dict[str, ConversationChain] = []

def createPrompt(human_name: str, ai_name: str) -> ChatPromptTemplate:       
    template = f"너는 {human_name}의 친절한 친구이고, 너의 이름은 {ai_name}이야."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "{history}\n{input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    return chat_prompt

def useLLM(token: str) -> ChatOpenAI:
    return ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9, openai_api_key=token)


def createConversation(llm: ChatOpenAI, prompt: ChatPromptTemplate) -> ConversationChain:
    conversation = ConversationChain(
        llm=llm, prompt=prompt,
        memory=ConversationBufferWindowMemory()
    )
    return conversation
