import pytest
from api import app, users

@pytest.fixture
def client():
    app.config["TESTING"] = True
    # reset users dictionary before each test
    users.clear()
    with app.test_client() as client:
        yield client

def test_add_user(client):
    response = client.post("/users", json={ "id": 1, "name": "Alice" })

    assert response.status_code == 201
    assert response.json == { "id": 1, "name": "Alice" }

def test_get_user(client):
    client.post("/users", json={ "id": 2, "name": "John" })

    response = client.get("/users/2")

    assert response.status_code == 200
    assert response.json == { "id": 2, "name": "John" }

def test_get_user_not_found(client):
    response = client.get("/users/69")

    assert response.status_code == 404
    assert response.json == { "error": "User not found" }

def test_add_duplicate_user(client):
    client.post("/users", json={ "id": 1, "name": "Alice" })
    response = client.post("/users", json={ "id": 1, "name": "Alice" })

    assert response.status_code == 400
    assert response.json == { "error": "User already exists" }

