from models.customer import Customer
from models.user import User
from views.user_database import save_new_user_to_database


def registerCustomer(first_name, last_name, email, password, user_name):
    customer: User = Customer(first_name, last_name, email, password, user_name)
    save_new_user_to_database(customer)
