# this will contain the User class
class User:
    def __init__(self, first_name, last_name, email_address, password, phone_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = email_address
        self.__password = password
        self.__phone_number = phone_number

    def getfirst_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def getlast_name(self):
        return self.__last_name

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def get_email_address(self):
        return self.__email_address

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password

    # how to go

    def get_password(self):
        return self.__password

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number
