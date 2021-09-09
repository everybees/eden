import uuid


class Product:
    def __init__(self, name, price, product_desc, category, product_id=""):
        if product_id == "":
            self.__id = str(uuid.uuid4())
        else:
            self.__id = product_id
        self.__name = name
        self.__price = price
        self.__product_desc = product_desc
        self.__category = category

    @property
    def get__product_id(self):
        return self.__id

    @property
    def get__product_name(self):
        return self.__name

    @property
    def get__product_price(self):
        return self.__price

    @property
    def get__product_desc(self):
        return self.__product_desc

    @property
    def get__product_category(self):
        return self.__category