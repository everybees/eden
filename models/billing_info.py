from models.address import Address
from models.credit_card_info import Credit_Card_Info


class Billing_Info:
    def __init__(self, receiver_phone_number: str, receiver_last_name: str, receiver_first_name: str, delivery_address:
    Address, credit_card_info: Credit_Card_Info):
        self.__receiver_phone_number: str = receiver_phone_number
        self.__receiver_first_name: str = receiver_first_name
        self.__receiver_last_name: str = receiver_last_name
        self.__delivery_address: Address = delivery_address
        self.credit_card_info: Credit_Card_Info = credit_card_info

    def update__billing_info(self, phone_number: str = "", first_name: str = "", last_name=""):
        if phone_number != "":
            self.__receiver_phone_number = phone_number
        if first_name != "":
            self.__receiver_first_name = first_name
        if last_name != "":
            self.__receiver_last_name = last_name

    @property
    def get__receiver_first_name(self):
        return self.__receiver_first_name

    @property
    def get__receiver_last_name(self):
        return self.__receiver_last_name

    @property
    def get__receiver_phone_number(self):
        return self.__receiver_phone_number

    @property
    def get_delivery_address(self):
        return self.__delivery_address

    @property
    def get_card_info(self):
        return self.credit_card_info
