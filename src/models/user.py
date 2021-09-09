import abc


class User(abc.ABC):
    def __init__(self, first_name, last_name, email, password, phone="", address=None):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__home_address = address

    @property
    def get__first_name(self):
        return self.__first_name

    def set__first_name(self, first_name):
        self.__first_name = first_name

    @property
    def get__last_name(self):
        return self.__last_name

    def set__last_name(self, last_name):
        self.__last_name = last_name

    @property
    def get__password(self):
        return self.__password

    def set__password(self, password):
        self.__password = password

    @property
    def get__email(self):
        return self.__email

    def set__email(self, email):
        self.__email = email

    @property
    def get__phone(self):
        return self.__phone

    def set__phone(self, phone):
        self.__phone = phone

    @property
    def get__home_address(self):
        return self.__home_address

    def set__home_address(self, address):
        self.__home_address = address
