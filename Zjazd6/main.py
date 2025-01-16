from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


# Model użytkownika
class User(BaseModel):
    id: int
    name: str
    email: str


# Pseudo-baza danych
users_db: List[User] = [
    User(id=1, name="Jan Kowalski", email="jan@kowalski.pl"),
    User(id=2, name="Anna Nowak", email="anna@nowak.pl")
]


# Endpointy API
@app.get("/users", response_model=List[User])
def get_users():
    return users_db


@app.get("/users/{id}", response_model=User)
def get_user(id: int):
    for user in users_db:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users", response_model=User, status_code=201)
def create_user(user: User):
    if any(u.id == user.id for u in users_db):
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    users_db.append(user)
    return user


@app.put("/users/{id}", response_model=User)
def update_user(id: int, user: User):
    for index, existing_user in enumerate(users_db):
        if existing_user.id == id:
            users_db[index] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{id}", status_code=204)
def delete_user(id: int):
    for index, user in enumerate(users_db):
        if user.id == id:
            del users_db[index]
            return
    raise HTTPException(status_code=404, detail="User not found")


# Testy
import pytest
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == len(users_db)


def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Jan Kowalski"


def test_get_user_by_id_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404


def test_create_user():
    new_user = {"id": 3, "name": "Piotr Nowy", "email": "piotr@nowy.pl"}
    response = client.post("/users", json=new_user)
    assert response.status_code == 201
    assert response.json()["name"] == new_user["name"]


def test_create_user_duplicate_id():
    duplicate_user = {"id": 1, "name": "Duplicate", "email": "dup@kowska.pl"}
    response = client.post("/users", json=duplicate_user)
    assert response.status_code == 400


def test_update_user():
    updated_user = {"id": 1, "name": "Jan Zmieniony", "email": "jan@zmieniony.pl"}
    response = client.put("/users/1", json=updated_user)
    assert response.status_code == 200
    assert response.json()["name"] == updated_user["name"]


def test_update_user_not_found():
    non_existent_user = {"id": 999, "name": "Ghost", "email": "ghost@notfound.pl"}
    response = client.put("/users/999", json=non_existent_user)
    assert response.status_code == 404


def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 204
    response = client.get("/users/1")
    assert response.status_code == 404


def test_delete_user_not_found():
    response = client.delete("/users/999")
    assert response.status_code == 404
