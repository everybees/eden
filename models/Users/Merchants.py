import json

from models.Users.Exceptions import IncompleteDetails, InvalidCustomer, InvalidLoginDetails, UserExists, ProductExists
from models.Users.Users import User
from views.Product import Product


class Merchant(User):
    database_file = open("../../database.json", "r+")
    database_file_loaded = json.load(database_file)

    def __init__(self, company_name, password, email, company_reference_number):
        super().__init__()
        self.company_name = company_name
        self.email = email
        self.password = password
        self.company_reference_number = company_reference_number
        self.number_of_registered_merchants = 0
        self.is_logIn = True
        self.user_exists = True
        self.number_of_products = 0
        self.product_exists = True


    def set_merchant_password(self, password):
        self.password = password

    def get_merchant_password(self):
        return self.password

    def set_merchant_email(self, email):
        self.email = email

    def get_merchant_email(self):
        return self.email

    def display_merchant_company_name(self):
        return self.company_name

    def set_merchant_company_name(self, company_name):
        self.company_name = company_name

    def display_company_reference_number(self):
        return self.company_reference_number

    def register(self, company_name, email, password, reference_number):
        if company_name == "" or email == "" or password == "" or reference_number == "":
            raise IncompleteDetails("Incomplete registration details")
        self.check_if_user_exists(company_name, email, reference_number)
        merchant = Merchant(company_name, email, password, reference_number)
        merchant_data = {
            "company_name": company_name,
            "email": email,
            "password": password,
            "reference_number": merchant.company_reference_number
        }

        self.database_file_loaded['merchants'].append(merchant_data)
        self.database_file.seek(0)
        json.dump(self.database_file_loaded, self.database_file, indent=4)
        self.number_of_registered_merchants += 1

    def get_number_of_registered_merchants(self):
        return self.number_of_registered_merchants

    def merchant_login(self, company_name, password):
        merchants = self.database_file_loaded['merchants']
        for merchant in merchants:
            if company_name == merchant['company_name'] and password == merchant['password']:
                return self.is_logIn
        raise InvalidLoginDetails("In correct login detail try again")

    def check_if_user_exists(self, company_name, email, reference_number):
        merchants = self.database_file_loaded['merchants']
        for merchant in merchants:
            if company_name.casefold() == merchant['company_name']:
                raise UserExists("Company name already exists")
            elif email == merchant['email']:
                raise UserExists("Email already exists")
            elif reference_number == merchant['reference_number']:
                raise UserExists

    def add_product(self, product_name, product_price, product_description, quantity_available):
        if self.check_if_product_exists(product_name, product_description):
            raise ProductExists("Product already exists")
        products = Product(product_name, product_price, product_description, quantity_available)
        product_data = {
            "name": product_name,
            "price": product_price,
            "description": product_description,
            "quantity_available": quantity_available
        }
        self.database_file_loaded['products'].append(product_data)
        self.database_file.seek(0)
        json.dump(self.database_file_loaded, self.database_file, indent=4)
        self.number_of_products += 1

    def get_number_of_products(self):
        return self.number_of_products

    def display_product(self):
        products = self.database_file_loaded['products']
        for product in products:
            print(product)

    def check_if_product_exists(self, product_name, product_description):
        products = self.database_file_loaded['products']
        for product in products:
            if product_name.casefold() == product['name'] and product_description.casefold() == product['description']:
                return self.product_exists

