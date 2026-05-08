from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# models
from pydantic import BaseModel

app = FastAPI()

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
def add_todo(todo: Todo):
    todos.append(todo.model_dump())
    # print("todos:", todos)
    return {"message": "Todo added"}


@app.delete("/todos/{id}")
def delete_todo(id: int):
    todos.pop(id)
    return {"message": "Todo deleted!"}
