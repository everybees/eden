from unittest import TestCase

from exceptions.login_exception import Login_Exception
from views.user_database import find_customer_by_email, find_merchant_by_email
from views.user_function import register_user, login


class TestUser_Database(TestCase):
    def test_save_Customer(self):
        register_user(first_name="Ehis", last_name="Edemakhiota", user_name="ehizman",
                      password="EdemaEhi17.", email="edemaehiz@yahoo.com", customer_type="Customer")
        found_user = find_customer_by_email("edemaehiz@yahoo.com")
        self.assertIsNotNone(found_user)
        register_user(first_name="Eseosa", last_name="Edemakhiota", user_name="eseosa",
                      password="EdemaEhi17.", email="edemaeseosa@yahoo.com", customer_type="Customer")

    def test_save_Merchant(self):
        register_user(first_name="Micheal", last_name="Friday", user_name="mStore",
                      password="1234", email="michaelfriday@gmail.com", customer_type="Merchant")
        found_user = find_merchant_by_email("michaelfriday@gmail.com")
        self.assertIsNotNone(found_user)