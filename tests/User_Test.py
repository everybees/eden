import unittest

from models.User import User


class MyTestCase(unittest.TestCase):

    @classmethod
    # This test runs before every test to create a new object of user
    def setUp(cls) -> None:
        first_name = "Oluwatobi"
        last_name = "Jolayemi"
        email_address = "jolayemi.tobi@gmail.com"
        password = "123456"
        phone_number = "08166863770"
        cls.user = User(first_name, last_name, email_address, password, phone_number)

    def test_User_Can_Be_Created(self):
        self.assertEqual("Oluwatobi", self.user.getfirst_name())

    def test_that_user_can_set_first_name(self):
        self.user.set_first_name("Isaiah")
        self.assertEqual("Isaiah", self.user.getfirst_name())

    def test_that_user_can_set_lastname(self):
        self.user.set_last_name("Moses")
        self.assertEqual("Moses", self.user.getlast_name())

    def test_that_user_can_set_email_address(self):
        self.user.set_email_address("tobi@gmail.com")
        self.assertEqual("tobi@gmail.com", self.user.get_email_address())

    def test_that_user_change_password(self):
        self.user.change_password("123456", "23456")
        self.assertEqual("23456", self.user.get_password())

    def test_that_user_can_set_phone_number(self):
        self.user.set_phone_number("09074631010")
        self.assertEqual("09074631010", self.user.get_phone_number())


if __name__ == '__main__':
    unittest.main()
