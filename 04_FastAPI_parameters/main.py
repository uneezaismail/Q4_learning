from fastapi import FastAPI, Path , Query, Body, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Root route
@app.get("/")
async def home():
    return {"message": "Welcome to the Item API! Use /items/{item_id} to get item details."}


# Path Parameter Validation
@app.get("/items/{item_id}")
async def get_item(
    item_id: int = Path(
        ...,  # Required parameter
        title="Item Identifier",
        description="The unique number assigned to each item. Must be 1 or higher.",
        ge=1
    )
):
    return {"message": f"Item {item_id} fetched successfully!"}




# query parameter validation
@app.get("/items/")
async def read_items(
    q: str | None = Query(
        None,  # ByDefault None (optional parameter)
        title="Search query",
        description="Type a keyword to look up relevant items",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0, description="How many items to skip from the start"),
    limit: int = Query(10, le=100, description="Maximum number of items to return")
):
    return {"q": q, "skip": skip, "limit": limit}



#  Multiple Parameters  
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(
        ..., 
        title="Item Unique Identifier", 
        ge=1),
    q: str | None = Query(None, min_length=3, description="Search query to filter items"),
    item: Item | None = Body(None, description="Optional item details in JSON format")
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result


#  Header Parameter 
@app.get("/items/{item_id}/header")
async def get_item_with_header(
    item_id: int = Path(
        ..., 
        title="Item Identifier", 
        ge=1),
    user_agent: Optional[str] = Header(None, title="User-Agent", description="The User-Agent string of the client")
):
    return {"item_id": item_id, "user_agent": user_agent}