from pydantic import BaseModel, Field
from typing import Annotated

class Pastry(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=50, description="Название товара")]
    price: Annotated[float, Field(gt=1, lt=100, description="Цена товара")]
    ingredient_list: list[Annotated[str,Field(min_length=2, max_length=100, description="Ингредиент")]]