from fastapi.testclient import TestClient


def test_healthcheck_ok(client: TestClient):
    response = client.get("/healthcheck")
    assert response.status_code == 200, response.json()
    assert response.json()["status"] == "success"


def test_one_message(client: TestClient):
    data = {
        "message": "First",
        "history": [{"message": "First", "author": "Client"}],
    }
    response = client.post("/", json=data)
    assert response.status_code == 200, response.json()
    assert response.json() == {"message": "Agent response"}


def test_three_messages(client: TestClient):
    data = {
        "message": "Second",
        "history": [
            {"message": "First", "author": "Client"},
            {"message": "First response", "author": "Agent"},
            {"message": "Second", "author": "Client"},
        ],
    }
    response = client.post("/", json=data)
    assert response.status_code == 200, response.json()
    assert response.json() == {"message": "Agent response"}


def test_agent_first(client: TestClient):
    data = {
        "message": "Third",
        "history": [
            {"message": "First response", "author": "Agent"},
            {"message": "First", "author": "Client"},
            {"message": "Second", "author": "Client"},
            {"message": "Second response", "author": "Agent"},
            {"message": "Third", "author": "Client"},
        ],
    }
    response = client.post("/", json=data)
    assert response.status_code == 400, response.json()
    assert response.json() == {"detail": "Invalid chat history"}


def test_double_user(client: TestClient):
    data = {
        "message": "Third",
        "history": [
            {"message": "First", "author": "Client"},
            {"message": "First response", "author": "Agent"},
            {"message": "Second", "author": "Client"},
            {"message": "Third", "author": "Client"},
            {"message": "Second response", "author": "Agent"},
        ],
    }
    response = client.post("/", json=data)
    assert response.status_code == 400, response.json()
    assert response.json() == {"detail": "Invalid chat history"}


def test_double_agent(client: TestClient):
    data = {
        "message": "Third",
        "history": [
            {"message": "First", "author": "Client"},
            {"message": "First response", "author": "Agent"},
            {"message": "Second response", "author": "Agent"},
            {"message": "Second", "author": "Client"},
        ],
    }
    response = client.post("/", json=data)
    assert response.status_code == 400, response.json()
    assert response.json() == {"detail": "Invalid chat history"}


def test_only_agent(client: TestClient):
    data = {
        "message": "Third",
        "history": [
            {"message": "First response", "author": "Agent"},
        ],
    }
    response = client.post("/", json=data)
    assert response.status_code == 400, response.json()
    assert response.json() == {"detail": "Invalid chat history"}
