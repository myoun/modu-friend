from fastapi import FastAPI
from dotenv import load_dotenv
from src.lib.chain import useLLM, createConversation, createPrompt, conversations
import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
app = FastAPI()

llm = useLLM(token=OPENAI_TOKEN)
conversation = createConversation(llm, prompt=createPrompt("철수", "영희"))

@app.get("/")
def root():
    return conversation.predict(input="안녕")

@app.on_event('shutdown')
def on_shutdown():
    pass