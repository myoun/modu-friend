from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from .main import app, get_db
from .database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try: 
            yield session
        finally:
            session.close()
    
    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)


def test_create_user(client: TestClient):
    response = client.post("/api/auth/user", json={"id": "testuser10", "name" : "John", "password" : "john1234"})

    assert response.status_code == 200

    return response.json()


def test_login_user(client: TestClient):
    created_user = test_create_user(client)["user"]

    login_user_response = client.post("/api/auth/login", json={"id": "testuser10", "password": "john1234"})

    assert login_user_response.status_code == 200

    logined_user = login_user_response.json()["user"]

    assert created_user == logined_user

    return logined_user

def test_create_friend(client: TestClient):
    logined_user = test_login_user(client)
    create_friend_response = client.post("/api/ai/friend", json={"name": "ai1", "friend_of": logined_user["id"], "mbti" : "INTP", "gender": "male"})

    assert create_friend_response.status_code == 200

    created_friends = create_friend_response.json()

    return created_friends

def test_get_friend_info(client: TestClient):
    created_friend = test_create_friend(client)[0]

    get_friend_info_response = client.get("/api/ai/friend/info", params=[("friend_id", created_friend["id"])])

    assert get_friend_info_response.status_code == 200

    friend_info = get_friend_info_response.json()

    assert created_friend["id"] == friend_info["id"]

    return friend_info

def test_get_friend_conversation(client: TestClient):
    friend_info = test_get_friend_info(client)

    get_friend_conversation_response = client.get("/api/ai/friend/conversation", params=[("friend_id", friend_info["id"])])

    assert get_friend_conversation_response.status_code == 200

    friend_conversation = get_friend_conversation_response.json()

    assert type(friend_conversation) == list

def test_post_friend_conversation(client: TestClient):
    user_info = test_login_user(client)
    friend_info = test_get_friend_info(client)
    print(user_info, friend_info)

    post_friend_conversation_response = client.post("/api/ai/friend/conversation", json={"friend_id": friend_info["id", "user_id": user_info["id"], "message": "hi"]})
    
    assert post_friend_conversation_response.status_code == 200