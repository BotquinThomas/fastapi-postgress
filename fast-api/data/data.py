from ..schemas.schemas import Item, ListItems
import pandas as pd

list_items = [
    Item(**{"id": 1,
     "name": "computer",
     "price": 2000,
     "type": "electronics"}),
    Item(**{"id": 2,
     "name": "laptop",
     "price": 1000,
     "type": "electronics"}),
    Item(**{"id": 3,
     "name": "dishwasher",
     "price": 1500,
     "type": "electronics"})
]
 
list_items = ListItems(**{"list_items": list_items})

df_items_food = pd.DataFrame(
    {"name" : ["chicken", "eggs", "pasta"],
     "price": [6,1,2],
     "type" : "food"}
)