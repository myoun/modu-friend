from langchain.memory.chat_message_histories import SQLChatMessageHistory
from mfriend.main import settings
from mfriend.ai import schemas
from uuid import UUID

CONNECTION_STRING = settings.DB_URL


def get_chat_message_history(user_id: str, friend_id: UUID) -> SQLChatMessageHistory:
    session_id = f"{user_id}_{friend_id}"

    return SQLChatMessageHistory(
        session_id=session_id,
        connection_string=CONNECTION_STRING
    )

def get_chat_message_history_by_friend(friend: schemas.FriendSchema) -> SQLChatMessageHistory:
    return get_chat_message_history(friend.friend_of, friend.id)