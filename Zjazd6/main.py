from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()


# Model użytkownika
class User(BaseModel):
    name: str
    email: EmailStr


# Pseudo-baza danych
users_db = [
    {"id": 1, "name": "Jan Kowalski", "email": "jan@kowalski.pl"},
    {"id": 2, "name": "Anna Nowak", "email": "anna@nowak.pl"}
]


# Endpointy API
@app.get("/users", response_model=List[dict])
def get_users():
    return users_db


@app.get("/users/{id}", response_model=dict)
def get_user(id: int):
    user = next((u for u in users_db if u["id"] == id), None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users", response_model=dict, status_code=201)
def create_user(user: User):
    new_id = max(u["id"] for u in users_db) + 1 if users_db else 1
    new_user = {"id": new_id, "name": user.name, "email": user.email}
    users_db.append(new_user)
    return new_user


@app.put("/users/{id}", response_model=dict)
def update_user(id: int, user: User):
    for existing_user in users_db:
        if existing_user["id"] == id:
            existing_user["name"] = user.name
            existing_user["email"] = user.email
            return existing_user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{id}")
def delete_user(id: int):
    global users_db
    user = next((u for u in users_db if u["id"] == id), None)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    users_db = [u for u in users_db if u["id"] != id]
    return {"message": "User deleted"}
