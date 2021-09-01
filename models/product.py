import random

from exceptions.product_exception import Product_Exception
from models.product_category import Product_Category


class Product:
    def __init__(self, product_name: str, price: float, product_description: str, product_category: str):
        if product_category == "groceries":
            self.__category = Product_Category.GROCERIES
        elif product_category == "electronics":
            self.__category = Product_Category.ELECTRONICS
        elif product_category == "utensils":
            self.__category = Product_Category.UTENSILS
        elif product_category == "clothing":
            self.__category = Product_Category.CLOTHING
        else:
            raise Product_Exception("Invalid product category")
        self.__description = product_description
        self.__price = price
        self.__product_name = product_name
        self.__id = "SKU-" + str(random.randint(0, 100000))

    @property
    def get__product_name(self) -> str:
        return self.__product_name

    @property
    def get__price(self) -> float:
        return self.__price

    @property
    def get__description(self) -> str:
        return self.__description

    @property
    def get__category(self) -> Product_Category:
        return self.__category

    @property
    def get__id(self):
        return self.__id
