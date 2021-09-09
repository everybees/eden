from exceptions.login_exception import Login_Exception
from models.customer import Customer
from models.merchant import Merchant
from views.user_database import save_customer, find_customer_by_email, save_merchant


def register_user(first_name, last_name, email, password, user_name, customer_type):
    if customer_type == "Customer":
        customer = Customer(first_name=first_name, last_name=last_name, password=password, email=email)
        save_customer(customer=customer)
    elif customer_type == "Merchant":
        merchant = Merchant(first_name=first_name, last_name=last_name, password=password, email=email,
                            user_name=user_name)
        save_merchant(merchant)


def login(email, password):
    found_user = find_customer_by_email(email)
    if found_user is not None:
        if found_user.get__password == password:
            return True
    raise Login_Exception("Invalid details")
