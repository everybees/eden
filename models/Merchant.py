import json

from models.Product import Product
from models.Shop import Shop
from models.User import User


class Merchant(User):
    database_file = open("../../database.json", "r+")
    database_file_loaded = json.load(database_file)

    def __init__(self, first_name, last_name, email_address, password, phone_number):
        super().__init__(first_name, last_name, email_address, password, phone_number)
        self.__shop = None

    def create_shop(self, shop_name):
        shop = Shop(shop_name)
        self.__shop = shop

    def get_shop(self):
        return self.__shop

    def create_new_product(self, product_name, product_description, product_price, product_category, shop_id):
        new_product = Product(product_name, product_description, product_price, product_category, shop_id)
        product = {
            "name": new_product.get_product_name(),
            "description": new_product.get_product_description(),
            "product_price": new_product.get_product_price(),
            "product_category": new_product.get_product_category(),
            "shop_id": new_product.get_shop_id()
        }
        self.database_file_loaded['products'].append(product)
        self.database_file.seek(0)

        json.dump(self.database_file_loaded, self.database_file, indent=4)
