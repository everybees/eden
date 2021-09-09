from exceptions.login_exception import Login_Exception
from models.customer import Customer
from models.merchant import Merchant
from views.user_database import save_user, find_user_by_email


def register_user(first_name, last_name, email, password, user_name, customer_type):
    user = None
    if customer_type == "Customer":
        user = Customer(first_name=first_name, last_name=last_name, password=password, email=email, user_name=user_name)
    elif customer_type == "Merchant":
        user = Merchant(first_name=first_name, last_name=last_name, password=password, email=email, user_name=user_name)
    save_user(user=user)


def login(email, password):
    found_user = find_user_by_email(email)
    if found_user is not None:
        if found_user.get("Password") == password:
            return True
    raise Login_Exception("Invalid details")
