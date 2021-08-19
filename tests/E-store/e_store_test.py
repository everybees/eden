import unittest

from models.Users.Customer import Customer
from models.Users.Users import User


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def setUp(self):
        self.user = User()
        self.customer = Customer("Titobi", "Ligali", "1234", "titobiloluwaligali2005@gmail.com", "09012958377")

    def tearDown(self):
        self.user = None

    def test_that_customer_has_info(self):
        self.customer.first_name = ""
        self.customer.last_name = ""
        self.customer.password = "1234"
        self.customer.email = "titobiloluwaligali2005@gmail.com"

    def test_that_customer_has_first_name(self):
        self.customer.get_first_name()
        self.customer.set_first_name("titobiloluwa")
        self.assertEqual("titobiloluwa", self.customer.get_first_name())

    def test_that_customer_has_last_name(self):
        self.customer.set_last_name("Ligali")
        self.assertEqual("Ligali", self.customer.get_last_name())

    def test_that_customer_email(self):
        self.customer.set_email("titobiloluwaligali2005@gmail.com")
        self.assertEqual("titobiloluwaligali2005@gmail.com",self.customer.get_email())




if __name__ == '__main__':
    unittest.main()
