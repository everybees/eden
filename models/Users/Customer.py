import json
import datetime

from models.Users.Exceptions import IncompleteDetails, InvalidCustomer
from models.Users.Users import User


class Customer(User):
    database_file = open("../../database.json", "r+")
    database_file_loaded = json.load(database_file)

    def __init__(self, first_name, last_name, email, password, phone_number):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.is_registered = True
        self.isLogin = True
        self.date = datetime.datetime.now()

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    number_of_registered_customer = 0

    def register(self, first_name, last_name, email, password, phone_number):
        if first_name == "" or last_name == "" or email == "" or password == "" or phone_number == "":
            raise IncompleteDetails("Please check that your details are complete")
        else:
            customer = Customer(first_name, last_name, email, password, phone_number)
            customer_data = {
                "name": customer.first_name + " " + last_name,
                "email": customer.email,
                "password": customer.password,
                "phone_number": customer.phone_number
            }
            self.database_file_loaded['customers'].append(customer_data)

            self.database_file.seek(0)

            json.dump(self.database_file_loaded, self.database_file, indent=4)
        self.number_of_registered_customer += 1
        return self.is_registered

    def get_number_of_registered_customer(self):
        return self.number_of_registered_customer

    def login(self, email_address, password):
        customers = self.database_file_loaded['customers']
        for customer in customers:
            if email_address == customer['email'] and password == customer['password']:
                return self.isLogin
            else:
                raise InvalidCustomer("Please check that your email and  password is correct")
        return self.isLogin

