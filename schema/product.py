from typing import Union

from pydantic import BaseModel

class ProductSchema(BaseModel):
    product_id: int
    name: str
    price: float
    currency: str
    category: Union[str, None]
    brand: Union[str, None]
    
