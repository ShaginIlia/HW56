from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


# Получить всех пользователей
@app.get("/users")
async def get_all_users() -> dict:
    return users


# Зарегистрировать нового пользователя
@app.post("/user/{username}/{age}")
async def registered_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:

    new_user_id = str(int(max(users, key=int)) + 1)
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return f'User {new_user_id} is registered'


# Обновить данные пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: str,
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:

    if user_id not in users:
        return f"User with id {user_id} not found"
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f'The user {user_id} is updated'


# Удалить пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    if user_id not in users:
        return f"User with id {user_id} not found"
    users.pop(user_id)
    return f'User with id {user_id} was deleted.'
