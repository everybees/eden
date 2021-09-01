class Registration_Dto:
    def __init__(self, firstname: str, lastname: str, email: str, password: str):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password

    @property
    def get__firstname(self):
        return self.__firstname

    @property
    def get__lastname(self):
        return self.__lastname

    @property
    def get__email(self):
        return self.__email

    @property
    def get__password(self):
        return self.__password
