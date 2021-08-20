from models.User import user
from models.merchant import Merchant
from models.customer import Customer


def create_user(firstname, lastname, id, email, password, usertype):
    user.__init__(firstname, lastname, id, email, password, usertype)


def create_merchant(firstname, lastname, id, email, password, usertype, billing_address, card_details, shop):
    Merchant.__init__(firstname, lastname, id, email, password, usertype, billing_address, card_details, shop)


def create_customer(firstname, lastname, id, email, password, usertype, billing_address, card_details):
    Customer.__init__(firstname, lastname, id, email, password, usertype, billing_address, card_details)
