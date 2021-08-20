import datetime

from models.Users.Cart import Cart
from models.Users.Customer import Customer
from models.Users.Exceptions import IncompleteDetails, InvalidCustomer
from models.Users.Item import Item


class Platform:
    list_of_customers = []
    customer = Customer
    carts = []

    def __init__(self):
        self.is_registered = True
        self.isLogin = True
        self.date = datetime.datetime.now()

    def register(self, first_name, last_name, email, password, phone_number):
        if first_name == "" or last_name == "" or email == "" or password == "" or phone_number == "":
            raise IncompleteDetails("Please check that your details are complete")
        else:
            customer = Customer(first_name, last_name, email, password, phone_number)
            self.list_of_customers.append(customer)
        return self.is_registered

    def login(self, email_address, password):
        for self.Customer in self.list_of_customers:
            if email_address == self.Customer.email and password == self.Customer.password:
                return self.isLogin
            else:
                raise InvalidCustomer("Please check that your email and  password is correct")
        return self.isLogin

    def add_to_cart(self, item):
        item = Item()
        cart = Cart(item)
        self.cart.append(cart)

