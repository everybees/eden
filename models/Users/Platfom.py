from models.Users.Customer import Customer
from models.Users.Exceptions import IncompleteDetails


class Platform:
    list_of_customers = []

    def __init__(self):
        self.is_registered = True

    def register(self, first_name, last_name, email, password, phone_number):
        if first_name == "" or last_name == "" or email == "" or password == "" or phone_number == "":
            raise IncompleteDetails("Please check that your details are complete")
        else:
         customer = Customer(first_name, last_name, email, password, phone_number)
         self.list_of_customers.append(customer)
        return self.is_registered

