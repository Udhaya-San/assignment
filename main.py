from typing import Optional

from fastapi import FastAPI

app = FastAPI(
    title="Basic FastAPI App",
    description="A small first API with a root endpoint and endpoints that take URL values.",
    version="1.0",
)


@app.get("/")
def read_root():
    """Root endpoint: returns a welcome message."""
    return {"message": "Hello, FastAPI"}


@app.get("/greet/{name}")
def greet(name: str):
    """Path parameter: /greet/Udhay -> greets that name."""
    return {"message": f"Hello, {name}!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """Path parameter (item_id) plus an optional query parameter (q).

    Example: /items/5?q=pen
    """
    return {"item_id": item_id, "q": q}


@app.get("/add")
def add(a: float, b: float):
    """Query parameters: /add?a=10&b=15 -> returns the sum."""
    return {"a": a, "b": b, "result": a + b}