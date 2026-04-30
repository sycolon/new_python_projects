from dataclasses import dataclass
from datetime import datetime

@dataclass
class Product:
    id:int
    name:str
    price:float

    def __str__(self):
        # 9385: Dell Laptop - Price: 599.99€
        return f"{self.id}:  {self.name} - Price: {self.price}€"


@dataclass
class PhysicalProduct(Product):
    weight:float
    stock:int=0

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative!")
        if self.weight <= 0:
            raise ValueError("Weight cannot be zero or less")
        if self.stock < 0:
            raise ValueError("Stock cannot be negative!")

    def __str__(self):
        return super().__str__() + f"Stock: {self.stock}"


@dataclass
class DigitalProduct(Product):
    license_key:str
    expiry_date:datetime

