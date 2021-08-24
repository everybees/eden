class Product:
    def __init__(self, product_name, product_description, product_price, product_category, shop_id):
        self.__product_name = product_name
        self.__product_description = product_description
        self.__product_price = product_price
        self.__product_category = product_category
        self.__shop_id = shop_id

    def get_product_name(self):
        return self.__product_name

    def get_product_description(self):
        return self.__product_description

    def get_product_price(self):
        return self.__product_price

    def get_product_category(self):
        return self.__product_category

    def get_shop_id(self):
        return self.__shop_id
