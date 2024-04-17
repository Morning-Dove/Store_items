from pydantic import BaseModel

class StoreItems(BaseModel):
    id: int
    name: str
    description: str
    price: float
