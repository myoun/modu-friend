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

@pytest.fixture()
def test_user(client: TestClient):
    response = client.post("/api/auth/user", json={"id": "testuser1", "name" : "John", "password" : "john1234"})

    return response.json()["user"]

@pytest.fixture()
def test_friend(client: TestClient, test_user):
    create_friend_response = client.post("/api/ai/friend", json={"name": "ai1", "friend_of": test_user["id"], "mbti" : "INTP", "gender": "male"})

    assert create_friend_response.status_code == 200

    created_friends = create_friend_response.json()

    return created_friends[0]

def test_login_user(client: TestClient, test_user):

    login_user_response = client.post("/api/auth/login", json={"id": test_user["id"], "password": "john1234"})

    assert login_user_response.status_code == 200

    logined_user = login_user_response.json()["user"]

    assert test_user == logined_user

def test_get_friend_info(client: TestClient, test_friend):

    get_friend_info_response = client.get("/api/ai/friend/info", params=[("friend_id", test_friend["id"])])

    assert get_friend_info_response.status_code == 200

    friend_info = get_friend_info_response.json()

    assert test_friend["id"] == friend_info["id"]

def test_get_friend_conversation(client: TestClient, test_friend):

    get_friend_conversation_response = client.get("/api/ai/friend/conversation", params=[("friend_id", test_friend["id"])])

    assert get_friend_conversation_response.status_code == 200

    friend_conversation = get_friend_conversation_response.json()

    assert type(friend_conversation["conversation"]) == list

def test_post_friend_conversation(client: TestClient, test_user, test_friend):

    post_friend_conversation_response = client.post("/api/ai/friend/conversation/", json={"friend_id": test_friend["id"], "user_id": test_user["id"], "message": "hi"})
    
    assert post_friend_conversation_response.status_code == 200

    post_friend_conversation = post_friend_conversation_response.json()

    assert type(post_friend_conversation["message"]) == str