# standard imports
import os
import sys

# imports from folders
from .schemas.schemas import Item, ListItems, CreateItem
from .data.data import list_items, df_items_food
from .config.config import config

# third party imports
from fastapi import FastAPI, Path, Query, HTTPException
import uvicorn
from typing import Optional, List
from pydantic import BaseModel
import sqlalchemy
import pandas as pd
import psycopg2
import databases


app = FastAPI()

# Hello World
@app.get("/")
async def landind_page() -> dict:
    return {"Hello": "World5",
            "Documentation": "http://localhost:80/docs",
            }

# Path parameters
@app.get("/get_item/{item_id}", response_model = Item)
async def get_item(
     item_id: int = Path(..., title="The ID of the item to get")
     ) -> dict:
     for item in list_items.list_items:
          if item_id == item.id:
               return item
     else:
          raise HTTPException(status_code = 404,
                              detail = "This item_id does not exist") 

# Query parameters
@app.get("/get_item", response_model = Item)
async def get_item(
     item_id: int = Query(..., title="The ID of the item to get")
     ) -> dict:
     for item in list_items.list_items:
          if item_id == item.id:
               return item
     else:
          raise HTTPException(status_code = 404,
                              detail = "This item_id does not exist") 

# Pydantic models 
@app.get("/get_all_items", response_model = ListItems)
async def get_all_items():
     return {'list_items' : list_items.list_items}
     
# Post query using pidantic models
@app.post("/add_item/", status_code = 201,response_model = Item)
async def add_item(
     item_in : CreateItem) -> dict:
     """
     Create a new recipe (in memory only)
     """
     from data.data import list_items
     new_id = len(list_items.list_items) + 1
     new_item = Item(**{
          "id" : new_id,
          "name": item_in.name,
          "price": item_in.price,
          "type": item_in.type
     })
     list_items = {"list_items": list_items.list_items.append(new_item)}
     return new_item.dict()

###  interact with postgresql using the REST API  ###

# configure engine
_config = config(filename = 'config/database.ini', section = "postgresql")
DATABASE_URL = str(sqlalchemy.engine.url.URL.create(**_config))
database = databases.Database(DATABASE_URL)

# add event handler to connect to and disconnect from postgres
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# query shakespeare dataset using get method
@app.get("/get_shakespeare/")
async def get_shakespeare() -> dict:
     #_config = config(filename = 'config/database.ini', section = "postgresql")
     #engine = sqlalchemy.create_engine(url = sqlalchemy.engine.url.URL.create(**_config))
     #with engine.connect() as conn:
     query = """
     SELECT id, title, year, genre_type
     FROM shakespeare.work AS a
     WHERE year = ( SELECT MAX(year) FROM shakespeare.work );
     """
     return await database.fetch_all(query)

def insert_df_into_table(df: pd.DataFrame,table_name: str):
     # transform df into a format that is suitable for database.execute_many()
     # https://github.com/encode/databases
     query = f"INSERT INTO {table_name} ({','.join(df.columns)}) VALUES ({','.join([f':{col}' for col in df.columns])})"
     values = [row.to_dict() for _ , row in df.iterrows()]
     return query, values

# insert values into item dataset through post method
@app.post("/add_items_to_db/", status_code = 201)
async def add_items_to_db():
     # get max index
     max_i = int(await database.execute("SELECT max(id) AS max_i FROM items;"))
     # increment index before sending to sql
     df_items_food['id'] = range(max_i+1, len(df_items_food)+max_i+1)
     # insert into items
     #df_items_food.to_sql("items",DATABASE_URL, index = False,if_exists="append")  # using pandas to_sql method (not asynchroon)
     query, values = insert_df_into_table(df = df_items_food, 
                                          columns = df_items_food.columns, 
                                          table_name="items")
     
     await database.execute_many(query = query, values = values)
     return df_items_food.to_json()

# get items from db
@app.get("/get_items_from_db/", status_code = 200)
async def get_items_from_db():
     return await database.fetch_all("SELECT * FROM items")

# use asynchroon to chain get requests from linkedin job descriptions
     


     
     
     
     