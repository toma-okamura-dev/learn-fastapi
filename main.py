from typing import List, Union
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    title: Union[str, None] = None
    details: Union[str, None] = None
    cost: Union[float, None] = None
    discount: float = 5.0
    categories: List[str] = []


inventory = {
    "alpha": {"title": "Alpha", "cost": 25.5},
    "beta": {"title": "Beta", "details": "Top-rated product", "cost": 45.0, "discount": 8.5},
    "gamma": {"title": "Gamma", "details": None, "cost": 32.0, "discount": 5.0, "categories": []},
}


@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: str):
    return inventory[product_id]


@app.patch("/products/{product_id}", response_model=Product)
async def modify_product(product_id: str, product: Product):
    stored_product_data = inventory[product_id]
    stored_product_model = Product(**stored_product_data)
    update_data = product.dict(exclude_unset=True)
    updated_product = stored_product_model.copy(update=update_data)
    inventory[product_id] = jsonable_encoder(updated_product)
    return updated_product
