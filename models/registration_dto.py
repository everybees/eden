class Registration_Dto:
    def __init__(self, first_name: str, last_name: str, email: str, username: str, password: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__username = username
        self.__password = password

    @property
    def get__first_name(self):
        return self.__first_name

    @property
    def get__last_name(self):
        return self.__last_name

    @property
    def get__user_name(self):
        return self.__user_name

    @property
    def get__email(self):
        return self.__email

    @property
    def get__password(self):
        return self.__password
