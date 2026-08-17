from src.model.baker import Baker

_bakers =[
    Baker(name="Vladimir", second_name="Dudnikov", father_name="Pavlovich", age=20),
    Baker(name="Dmitriy", second_name="Dudnikov", father_name="Romanovich", age=18),
    Baker(name="Ivanov", second_name="Ivan", father_name="Ivanovich", age=30)
        ]

def get_all() -> list[Baker]:
    return _bakers

def get_one(name: str) -> Baker | None:
    for _baker in _bakers:
        if _baker.name == name:
            return _baker
    return None

def create(baker: Baker) -> Baker:
    return baker

def modify(baker: Baker) -> Baker:
    return baker

def replace(baker: Baker) -> Baker:
    return baker

def delete(name: str) -> bool:
    return None
