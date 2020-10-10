from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: int
    image: list
    description: str