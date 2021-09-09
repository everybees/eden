import json

from models.cart import Cart
from models.customer import Customer
from models.item import Item
from models.merchant import Merchant
from models.product import Product
from models.product_category import Product_Category


def serialize_product(product):
    if product.get__product_category is Product_Category.GROCERIES:
        product_category = "groceries"
    elif product.get__product_category is Product_Category.CLOTHING:
        product_category = "clothing"
    elif product.get__product_category is Product_Category.ELECTRONICS:
        product_category = "electronics"
    else:
        product_category = "utensils"

    return {
        "product_id": product.get__product_id,
        "product_name": product.get__product_name,
        "product_price": product.get__product_price,
        "product_category": product_category,
        "product_desc": product.get__product_desc
    }


def serialize_item(item):
    return {"quantity": item.get__quantity,
            "product": serialize_product(item.get__product)
            }


def serialize_cart(cart):
    _list = list()
    for item in cart.get_items_in_cart():
        _item = serialize_item(item)
        _list.append(_item)
    return _list


def serialize_user(user):
    if isinstance(user, Customer):
        return {
            user.get__email: {
                "type": type(user).__name__,
                "FirstName": user.get__first_name,
                "LastName": user.get__last_name,
                "Password": user.get__password,
                "Phone": user.get__phone,
                "Home Address": user.get__home_address,
                "Cart": serialize_cart(user.get__cart),
                "Billing Info": user.get__list_of_billing_info
            }
        }
    elif isinstance(user, Merchant):
        return {
            user.get__email: {
                "type": type(user).__name__,
                "FirstName": user.get__first_name,
                "LastName": user.get__last_name,
                "Password": user.get__password,
                "Phone": user.get__phone,
                "Home Address": user.get__home_address,
                "Products": user.get__list_of_products
            }
        }


def save_customer(customer):
    with open("/home/ehizman/PycharmProjects/eden/src/customers.json", 'r+', encoding='utf-8') as file_writer:
        user_details: dict = serialize_user(customer)
        _dict = json.load(file_writer)
        _dict.update(user_details)
        file_writer.seek(0)
        json.dump(_dict, file_writer, indent=4)
        file_writer.write("\n")


def save_merchant(merchant):
    with open("/home/ehizman/PycharmProjects/eden/src/merchants.json", 'r+', encoding='utf-8') as file_writer:
        user_details: dict = serialize_user(merchant)
        _dict = json.load(file_writer)
        _dict.update(user_details)
        file_writer.seek(0)
        json.dump(_dict, file_writer, indent=4)
        file_writer.write("\n")


def deserialize_product(_dict):
    product_id = _dict["product_id"]
    product_name = _dict["product_name"]
    product_price = _dict["product_price"]
    product_category = _dict["product_category"]
    product_desc = _dict["product_desc"]

    if product_category == "groceries":
        category = Product_Category.GROCERIES
    elif product_category == "clothing":
        category = Product_Category.CLOTHING
    elif product_category == "electronics":
        category = Product_Category.ELECTRONICS
    else:
        category = Product_Category.UTENSILS
    product = Product(name=product_name, product_desc=product_desc, product_id=product_id, price=product_price,
                      category=category)
    return product


def deserialize_item(item):
    quantity = item["quantity"]
    product = deserialize_product(item["product"])
    item = Item(quantity=quantity, product=product)
    return item


def deserialize_cart(_list):
    cart = Cart()
    for item in _list:
        item = deserialize_item(item)
        cart.add_item_to_cart(item=item)
    return cart


def deserialize_customer(_dict, email):
    first_name = _dict["FirstName"]
    last_name = _dict["LastName"]
    password = _dict["Password"]
    phone = _dict["Phone"]
    cart = _dict["Cart"]
    home_address = _dict["Home Address"]
    billing_info = _dict["Billing Info"]

    user = Customer(first_name=first_name, last_name=last_name, password=password, phone=phone,
                    cart=deserialize_cart(cart), email=email, home_address=home_address, list_of_billing_info=billing_info)
    return user


def find_customer_by_email(email):
    with open("/home/ehizman/PycharmProjects/eden/src/customers.json", 'r+', encoding='utf-8') as file_writer:
        _dict = json.load(file_writer)
        for key in _dict.keys():
            if key == email:
                return deserialize_customer(_dict.get(email), email)
        return None


def find_merchant_by_email(email):
    with open("/home/ehizman/PycharmProjects/eden/src/merchants.json", 'r+', encoding='utf-8') as file_writer:
        _dict = json.load(file_writer)
        for key in _dict.keys():
            if key == email:
                return _dict.get(email)
        return None
