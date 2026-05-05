from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/")
def home():
    return {"message": "Backend working!"}


@app.get("/todos")
def get_todos():
    # print("todos:", todos)
    return todos


@app.post("/todos")
def add_todo(todo: dict):
    todos.append(todo)
    # print("todos:", todos)
    return {"message": "Todo added"}
