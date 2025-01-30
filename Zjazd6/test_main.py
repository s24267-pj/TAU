from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Jan Kowalski"


def test_get_user_by_id_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404


def test_create_user():
    new_user = {"name": "Piotr Nowy", "email": "piotr@nowy.pl"}
    response = client.post("/users", json=new_user)
    assert response.status_code == 201
    assert response.json()["name"] == new_user["name"]


def test_create_user_invalid():
    response = client.post("/users", json={"name": "Brak Emaila"})
    assert response.status_code == 422  # FastAPI samo waliduje brakujące pola


def test_update_user():
    updated_user = {"name": "Jan Zmieniony", "email": "jan@zmieniony.pl"}
    response = client.put("/users/1", json=updated_user)
    assert response.status_code == 200
    assert response.json()["name"] == updated_user["name"]


def test_update_user_not_found():
    response = client.put("/users/999", json={"name": "Ghost", "email": "ghost@notfound.pl"})
    assert response.status_code == 404


def test_update_user_check():
    updated_user = {"name": "Jan Nowy", "email": "jan@nowy.pl"}
    client.put("/users/1", json=updated_user)
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == updated_user["name"]


def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted"


def test_delete_user_not_found():
    response = client.delete("/users/999")
    assert response.status_code == 404


def test_delete_user_check():
    client.delete("/users/1")
    response = client.get("/users/1")
    assert response.status_code == 404
