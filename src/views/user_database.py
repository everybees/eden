import json

from models.customer import Customer
from models.merchant import Merchant


def serialize_cart(cart):
    pass


def serialize_user(user):
    if isinstance(user, Customer):
        return {
            user.get__email: {
                "type": type(user).__name__,
                "FirstName": user.get__first_name,
                "LastName": user.get__last_name,
                "Password": user.get__password,
                "Username": user.get__user_name,
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
                "Username": user.get__user_name,
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


def find_customer_by_email(email):
    with open("/customers.json", 'r+', encoding='utf-8') as file_writer:
        _dict = json.load(file_writer)
        for key in _dict.keys():
            if key == email:
                return _dict.get(email)
        return None


def find_merchant_by_email(email):
    with open("/home/ehizman/PycharmProjects/eden/src/merchants.json", 'r+', encoding='utf-8') as file_writer:
        _dict = json.load(file_writer)
        for key in _dict.keys():
            if key == email:
                return _dict.get(email)
        return None
