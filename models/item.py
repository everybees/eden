from models.product import Product


class Item:
    def __int__(self, quantity: int, product: Product):
        self.__quantity = quantity
        self.__product = product

    @property
    def get__quantity(self):
        return self.__quantity

    @property
    def get__product(self):
        return self.__product
