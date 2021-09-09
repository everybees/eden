from unittest import TestCase

from views.customer_functions import registerCustomer


def test_register_function():
    first_name: str = "Ehis"
    last_name: str = "Edemakhiota"
    email: str = "edemaehiz@gmail.com"
    password: str = "EdemaEhi17."
    user_name: str = "ehizman"
    registerCustomer(first_name, last_name, email, password, user_name)


class Test(TestCase):
    test_register_function()
