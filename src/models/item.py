class Item:
    def __init__(self, quantity, product):
        self.__quantity = quantity
        self.__product = product

    @property
    def get__quantity(self):
        return self.__quantity

    @property
    def get__product(self):
        return self.__product

    def update_product_quantity(self):
        self.__quantity += 1
