class Item:
    def __init__(self, product_name: str, product_price: float, product_description: str):
        self.name = product_name
        self.price = product_price
        self.description = product_description

    def set_product_name(self, product_name):
        self.name = product_name

    def get_product_name(self):
        return self.name

    def set_product_price(self, product_price):
        self.name = product_price

    def get_product_name(self):
        return self.price

    def set_product_description(self, product_description):
        self.name = product_description

    def get_product_description(self):
        return self.description


