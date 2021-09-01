from typing import List

from models.billing_info import Billing_Info
from models.item import Item
from models.registration_dto import Registration_Dto
from models.shopping_cart import Shopping_Cart
from models.user import User
from views.customer_functions import update_customer


class Customer(User):
    def __init__(self, registration_dto: Registration_Dto):
        super(Customer, self).__init__(registration_dto.get__firstname, registration_dto.get__lastname,
                                       registration_dto.get__email, registration_dto.get__password)
        self.__list_of_billing_info: List[Billing_Info] = list()
        self.__shopping_cart: Shopping_Cart = Shopping_Cart()

    @property
    def get__list_of_billing_info(self):
        return self.__list_of_billing_info

    def update__list_of_billing_info(self, new_billing_info: Billing_Info):
        self.__list_of_billing_info.append(new_billing_info)
        update_customer(self, self.get__email)

    @property
    def get__shopping_cart(self):
        return self.__shopping_cart

    def add_to_cart(self, item: Item):
        self.__shopping_cart.add(item)
        update_customer(self, self.get__email)
