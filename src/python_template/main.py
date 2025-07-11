import os

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def health() -> None: ...


@app.get("/hello")
async def hello_world() -> str:
    return "Hello, World!"


def run() -> None:
    import uvicorn

    uvicorn.run(
        app,
        host=os.getenv("BACKEND__HOST__ADDRESS", "127.0.0.1"),
        port=os.getenv("BACKEND__HOST__PORT", 8080),
    )
