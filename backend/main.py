from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

# models
from pydantic import BaseModel

# connect to MongoDB
PORT = "mongodb://localhost:27017"
client = AsyncIOMotorClient(PORT)

# database
db = client.todo_db

# todo collection
todos_col = db.todos


origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = []


class Todo(BaseModel):
    title: str


# FastAPI handles request/response automatically.
# FastAPI automatically converts Python objects to JSON.
# FastAPI automatically converts and validates types.


@app.get("/")
def home():
    return {"message": "Backend working!"}


@app.get("/todos")
def get_todos():
    print("todos:", todos)
    return todos


@app.post("/todos")
async def add_todo(todo: Todo):
    # todos.append(todo.model_dump())
    # print("todos:", todos)
    await todos_col.insert_one(todo)
    return {"message": "Todo added"}


@app.delete("/todos/{id}")
def delete_todo(id: int):
    todos.pop(id)
    return {"message": "Todo deleted!"}
