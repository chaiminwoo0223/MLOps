from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Input Schema
class CreateIn(BaseModel):
    name: str
    nickname: str

# Output Schema
class CreateOut(BaseModel):
    status: str
    id: int

# FastAPI 인스턴스 생성
app = FastAPI()

# 사용자 DB
USER_DB = {}

# 예외 처리
NAME_NOT_FOUND = HTTPException(status_code=400, detail="Name not found.")

# Create
@app.post("/users", response_model=CreateOut)
def create_user(user: CreateIn) -> CreateOut:
    USER_DB[user.name] = user.nickname
    return CreateOut(status="success", id=len(USER_DB))

# Read
@app.get("/users")
def read_user(name: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    return {"nickname": USER_DB[name]}

# Update
@app.put("/users")
def update_user(name: str, nickname: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    USER_DB[name] = nickname
    return {"status": "success"}

# Delete
@app.delete("/users")
def delete_user(name: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    del USER_DB[name]
    return {"status": "success"}