from src.model.pastry import Pastry

_pastries =[
    Pastry(name="Bread", price=2, ingredient_list=["Flour","Water","Yeast","Salt"]),
    Pastry(name="Cake", price=10, ingredient_list=["Flour", "Sugar", "Eggs","Fat","Leaving Agent"]),
    Pastry(name="Cookie", price=4, ingredient_list=["Flour", "Fat","Sugar","Eggs"])
        ]

def get_all() -> list[Pastry]:
    return _pastries

def get_one(name: str) -> Pastry | None:
    for _pastry in _pastries:
        if _pastry.name == name:
            return _pastry
    return None

def create(pastry: Pastry) -> Pastry:
    return pastry

def modify(pastry: Pastry) -> Pastry:
    return pastry

def replace(pastry: Pastry) -> Pastry:
    return pastry

def delete(name: str) -> bool:
    return None