from models.merchant import Merchant
from models.customer import Customer
from models.shop import Shop


def signup_as_merchant(firstname, lastname, id, email, password, usertype, billing_address, card_details, shop):
    Merchant.__init__(firstname, lastname, id, email, password, usertype, billing_address, card_details, shop)


def signup_as_customer(firstname, lastname, id, email, password, usertype, billing_address, card_details):
    Customer.__init__(firstname, lastname, id, email, password, usertype, billing_address, card_details)


def create_shop(name, merchant_name, description, product, id):
    Shop.__init__(name, merchant_name, description, product, id)
