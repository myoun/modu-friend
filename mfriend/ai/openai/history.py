from langchain.memory.chat_message_histories import SQLChatMessageHistory
from mfriend.main import settings
from mfriend.ai import models


CONNECTION_STRING = settings.DB_URL


def get_chat_message_history(user_id: str, friend_id: int) -> SQLChatMessageHistory:
    session_id = f"{user_id}_{friend_id}"

    return SQLChatMessageHistory(
        session_id=session_id,
        connection_string=CONNECTION_STRING
    )

def get_chat_message_history_by_friend(friend: models.Friend) -> SQLChatMessageHistory:
    return get_chat_message_history(friend.friend_of, friend.id)