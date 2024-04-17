from fastapi import FastAPI

import json
from models import StoreItems

app = FastAPI()

with open("store_items.json", "r") as f:
    store_items_list = json.load(f)

store_items: list[StoreItems] = []

for item in store_items_list:
    store_items.append(StoreItems(**item))


@app.get("/store_items/")
async def get_items() -> list[StoreItems]:
    return store_items

@app.post("/store_items/")
async def create_items(item: StoreItems) -> None:
    store_items.append(item)

@app.put("/store_items/{item_id}")
async def update_items(item_id: int, updated_item: StoreItems) -> StoreItems:
    for i, item in enumerate(store_items):
        if item_id == item.id:
            store_items[i] = updated_item
            return updated_item

@app.delete("/store_items/{item_id}")
async def delete_items(item_id: int) -> str:
    for i, item in enumerate(store_items):
        if item.id == item_id:
            store_items.pop(i)
            return "Item deleted"

    
