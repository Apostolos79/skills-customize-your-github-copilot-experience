from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Item(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str] = None


# Simple in-memory storage
_items = []
_next_id = 1


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI items service"}


@app.get("/items/")
def list_items():
    return _items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in _items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items/", status_code=201)
def create_item(item: Item):
    global _next_id
    record = item.dict()
    record["id"] = _next_id
    _next_id += 1
    _items.append(record)
    return record


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for i, existing in enumerate(_items):
        if existing["id"] == item_id:
            updated = existing.copy()
            updated.update(item.dict(exclude_unset=True))
            updated["id"] = item_id
            _items[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for i, existing in enumerate(_items):
        if existing["id"] == item_id:
            _items.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item not found")
