class User_Dto:
    def __init__(self, firstname: str, lastname: str, email: str):
        self.__firstname: str = firstname
        self.__lastname: str = lastname
        self.__email: str = email
        # self.__password: str = password
        # self.__is_online: bool = is_online

    @property
    def get__firstname(self):
        return self.__firstname

    def set_firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def get__lastname(self):
        return self.__lastname

    def set_lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def get__email(self):
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    @property
    def is_online(self):
        return self.__is_online

    def set__is_online(self):
        self.__is_online = not self.is_online

    @property
    def get__password(self):
        return self.__password

    def set_password(self, password: str):
        self.__password = password
