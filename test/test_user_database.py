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

    def test_save_Merchant(self):
        register_user(first_name="Micheal", last_name="Friday", user_name="mStore",
                      password="1234", email="michaelfriday@gmail.com", customer_type="Merchant")
        found_user = find_merchant_by_email("michaelfriday@gmail.com")
        self.assertIsNotNone(found_user)

    def test_user_can_login(self):
        result = login("edemaehiz@yahoo.com", "EdemaEhi17.")
        self.assertTrue(result)

    def test_user_cannot_login_with_invalid_email(self):
        with self.assertRaises(Login_Exception):
            login("edemaehiz@gmail.com", "EdemaEhi17.")

    def test_user_cannot_login_with_invalid_password(self):
        with self.assertRaises(Login_Exception):
            login("edemaehiz@yahoo.com", "EdemaEhi.")


