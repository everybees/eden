import abc
from typing import List

from models.address import Address
from models.billing_info import Billing_Info


class User(abc.ABC):
    def __init__(self, first_name, last_name, email, user_name, password):
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__user_name: str = user_name
        self.__email: str = email
        self.__password: str = password
        self.__home_address: Address
        self.__phone_number: str

    @property
    def get__first_name(self):
        return self.__first_name

    def update_first_name(self, new_first_name: str):
        self.__first_name = new_first_name

    @property
    def get__last_name(self):
        return self.__last_name

    def update__last_name(self, new_last_name: str):
        self.__last_name = new_last_name

    @property
    def get__user_name(self):
        return self.__user_name

    def update_user_name(self, new_user_name: str):
        self.__user_name = new_user_name

    @property
    def get__email(self):
        return self.__email

    def update__email(self, new_email: str):
        self.__email = new_email

    @property
    def get__password(self):
        return self.__password

    def update__password(self, new_password: str):
        self.__password = new_password
