from .product import Product, PhysicalProduct, DigitalProduct
from datetime import datetime
from .out_of_stock_error import OutOfStockError
import time
#from typing import Dict, List

class Warehouse:
    def __init__(self):
        self.products = {} #:Dict[id:int, Product:object]
        self.history = []

    def add_product(self, product:Product):
        self.products[product.id] = product
        #self.history.append(f"{datetime.now()} {product.name} added!") # 2026-04-30 Lapto added!
        #self.history.append({int(datetime.timestamp(datetime.now())): f"{product.name} added."})
        self.history.append({int(time.time()): f"{product.name} added."})
    
    def sell_product(self, product_id:int, quantity:int) -> None:
        product = self.products.get(product_id)
        
        if not product: # if product == None
            print("Product not found!")
            return
        
        if isinstance(product, PhysicalProduct):
            if product.stock < quantity:
                raise OutOfStockError(f"We have only {product.stock} pieces from {product.name} in stock!")
            product.stock-=quantity

        self.history.append({int(time.time()): f"{quantity}x {product.name} sold."})


    @classmethod
    def create_warehouse_and_products(cls):
        warehouse = cls()
        warehouse.add_product(PhysicalProduct(354, "Dell X500", 979.99, 1.5,15))
        warehouse.add_product(DigitalProduct(632,"Hausmeister Kurs", 20.0,"BBQ-HM-2654-9875-x254",datetime(2029,10,30)))
       # warehouse.add_product(PhysicalProduct(354, "Dell X500", 979.99, 0,15)) # Error weight is 0
        return warehouse
    
    @staticmethod
    def calculate_tax(amount, tax_rate = 0.19) -> float:
        return round(amount * tax_rate, 2)