from pydantic import BaseModel, Field
from typing import Annotated

class Baker(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=100, description="Имя повара")]
    second_name: Annotated[str, Field(min_length=2, max_length=100, description="Фамилия повара")]
    father_name: Annotated[str, Field(min_length=2, max_length=100, description="Отчество повара")]
    age: Annotated[int, Field(gt=18,lt=70,description="Возраст повара")]