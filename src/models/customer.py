from models.cart import Cart
from src.models.user import User


class Customer(User):
    def __init__(self, first_name, last_name, email, password, phone="", cart=Cart(), home_address=None,
                 list_of_billing_info=None):
        super().__init__(first_name=first_name, last_name=last_name, email=email, password=password
                         , phone=phone, address=home_address)
        self.__cart = cart
        self.__list_of_billing_info = list_of_billing_info

    def add_to_cart(self, item):
        self.__cart.add_item_to_cart(item=item)

    @property
    def get__cart(self):
        return self.__cart

    def add_to_list_billing_info(self, billing_info):
        self.__list_of_billing_info.append(billing_info)

    @property
    def get__list_of_billing_info(self):
        return self.__list_of_billing_info