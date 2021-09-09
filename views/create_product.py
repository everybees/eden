from models.product import Product

global all_product

all_product = []


def create_product(name, category, description, price, discount):
    Product.__init__(name, category, description, price, discount)

    return Product


def add_product(name, category, description, price, discount):
    all_product.append(create_product(name, category, description, price, discount))

    return all_product


def remove_product(index):
    all_product.remove(index)

    return all_product


def view_product():
    print(all_product)
