from models.cart import Cart
from src.models.user import User


class Customer(User):
    def __init__(self, first_name, last_name, email, user_name, password):
        super().__init__(first_name, last_name, email, user_name, password)
        self.__cart = Cart()
        self.__list_of_billing_info = []

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