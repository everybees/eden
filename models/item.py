from models.product import Product


class Item:
    def __init__(self, quantity: int, product: Product):
        self.__quantity = quantity
        self.__product_id = product.get__id

    @property
    def get__quantity(self) -> int:
        return self.__quantity

    @property
    def get__product_id(self) -> str:
        return self.__product_id
