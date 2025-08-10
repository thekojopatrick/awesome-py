from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# for api validation


class Item(BaseModel):
    # text: str = None //not required
    text: str  # explict name required
    is_done: bool = False


items = []


@app.get('/')
def root():
    return {"Hello": "World"}


@app.post('/items')
def create_item(item: Item):
    items.append(item)
    return items


@app.get('/items', response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]


@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item {item_id} not found")
