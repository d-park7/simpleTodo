from typing import Union
from fastapi import FastAPI

app = FastAPI()

# Starting guide here: 
# https://fastapi.tiangolo.com/#installation


@app.get("/", description="Sample GET request")
def ping():
  # Standard get request, can return json data or string
  return "pong"

@app.post("/", description="Sample POST request", response_model=None)
def createItem(response_object: str):
  # Logic for creating an object, typically has a defined model
  pass

@app.put("/", description="Sample PUT request")
def updateItem(item_id: int):
  # Add logic for updating item with specified id
  pass

@app.delete("/", description="Sample DELETE request")
def deleteItem(item_id: int):
  # Add Logic for deleting item in database
  pass
