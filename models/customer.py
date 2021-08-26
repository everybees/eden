from dataclasses import dataclass
from typing import List

from models.billing_info import Billing_Info
from models.shopping_cart import Shopping_Cart
from models.user import User


class Customer(User):
    def __init__(self, first_name: str, last_name: str, email: str, user_name: str,password: str):
        super(Customer, self).__init__(first_name, last_name, user_name, email, password)
        self.__list_of_billing_info: List[Billing_Info] = list()
        self.__shopping_cart: List[Shopping_Cart] = list()

    @property
    def get__list_of_billing_info(self):
        return self.__list_of_billing_info

    def update__list_of_billing_info(self, new_billing_info: Billing_Info):
        self.__list_of_billing_info.append(new_billing_info)