from fastapi import FastAPI
from FastAPITutorial.basic.todo import todo_router


app = FastAPI()
app.include_router(todo_router)


@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }

