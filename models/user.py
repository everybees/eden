import abc

from exceptions.user_exception import UserException
from models.address import Address
from views.user_database_functions import find_user_in_database_by_email


def update_customer(user_details_update, email: str):
    if user_details_update is None:
        raise UserException("invalid parameters provided for update")
    elif (user_details_update.get__firstname == '') and (user_details_update.get__lastname == '') and (
            user_details_update.get__email == '') and (user_details_update.get__password == ''):
        raise UserException("invalid parameters provided for update")
    user_to_update = find_user_in_database_by_email(email=email)
    if user_to_update is None:
        raise UserException("No matching details found in database")
    else:
        if user_details_update.get__firstname != '':
            user_to_update.update_firstname(user_details_update.get__firstname)
        if user_details_update.get__lastname != '':
            user_to_update.update__lastname(user_details_update.get__lastname)
        if user_details_update.get__email != '':
            user_to_update.update__email(user_details_update.get__email)
        if user_details_update.get__password != '':
            user_to_update.update__password(user_details_update.get__password)


class User(abc.ABC):
    def __init__(self, firstname: str, lastname: str, email: str, password: str, is__online: bool = False):
        self.__firstname: str = firstname.capitalize()
        self.__lastname: str = lastname.capitalize()
        self.__email: str = email.lower()
        self.__password: str = password.lower()
        self.__home_address: Address = Address()
        self.__phone_number: str = ""
        self.__is_online: bool = is__online

    @property
    def is_online(self) -> bool:
        return self.__is_online

    def set__is_online(self):
        self.__is_online = not self.__is_online
        update_customer(self, self.__email)

    @property
    def get__phone_number(self):
        return self.__phone_number

    def update_phone_number(self, new_phone_number: str):
        self.__firstname = new_phone_number
        update_customer(self, self.__email)

    @property
    def get__home_address(self):
        return self.__home_address

    def update_home_address(self, new_home_address: Address):
        self.__firstname = new_home_address
        update_customer(self, self.__email)

    @property
    def get__firstname(self):
        return self.__firstname

    def update_firstname(self, new_firstname: str):
        self.__firstname = new_firstname
        update_customer(self, self.__email)

    @property
    def get__lastname(self):
        return self.__lastname

    def update__lastname(self, new_lastname: str):
        self.__lastname = new_lastname
        update_customer(self, self.__email)

    @property
    def get__email(self):
        return self.__email

    def update__email(self, new_email: str):
        self.__email = new_email
        update_customer(self, self.__email)

    @property
    def get__password(self):
        return self.__password

    def update__password(self, new_password: str):
        self.__password = new_password
        update_customer(self, self.__email)

