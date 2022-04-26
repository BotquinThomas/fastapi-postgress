from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    id: int
    name: str
    price: float
    type: str
    
class CreateItem(BaseModel):
    name: str
    price: float
    type: str
    
class ListItems(BaseModel):
     list_items: List[Item]
    
    