from models.BillingInfo import BillingInfo
from models.User import User


class Customer(User):
    def __init__(self, first_name, last_name, email_address, password, phone_number):
        super().__init__(first_name, last_name, email_address, password, phone_number)
        self.__billing_info = None

    def set_billing_info(self, address, card_info):
        billing_info = BillingInfo(address, card_info)
        self.__billing_info = billing_info

    def get_billing_info(self):
        return self.__billing_info
