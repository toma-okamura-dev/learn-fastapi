from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{a}") # a はパスパラメータです
async def read_user_item(
    a: str, b: str, c: int = 0, d: int | None = None #　bはクエリパラメータで、cはオプショナルなクエリパラメータです
):
    item = {"a": a, "b": b, "c": c, "d": d}
    return item