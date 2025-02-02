from typing import Optional

from fastapi import FastAPI

app = FastAPI()

print("erwerwer")
@app.get("/")
def read_root():
    return {"Hello": "World", "MyName": "Lek CodeMobiles"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}