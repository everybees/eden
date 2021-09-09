import abc


class User(abc.ABC):
    def __init__(self, first_name, last_name, email, user_name, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__user_name = user_name
        self.__password = password

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
    def get__user_name(self):
        return self.__user_name

    def set__user_name(self, user_name):
        self.__user_name = user_name

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



