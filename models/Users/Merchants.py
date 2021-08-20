from models.Users.Users import User


class Merchant(User):
    def __init__(self, company_name, password, email,  company_reference_number):
        super().__init__()
        self.company_name = company_name
        self.email = email
        self.password = password
        self. company_reference_number = company_reference_number

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
        return self.ompany_reference_number

    def registered_merchants(self):



