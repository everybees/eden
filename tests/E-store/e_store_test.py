import unittest

from models.Users.Customer import Customer
from models.Users.Exceptions import IncompleteDetails
from models.Users.Platfom import Platform
from models.Users.Users import User


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def setUp(self):
        self.user = User()
        self.customer = Customer("Titobi", "Ligali", "1234", "titobiloluwaligali2005@gmail.com", "09012958377")
        self.platform = Platform()

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
        self.assertEqual("titobiloluwaligali2005@gmail.com", self.customer.get_email())

    def test_that_customer_has_password(self):
        self.customer.set_password("1234")
        self.assertEqual("1234", self.customer.get_password())

    def test_that_customer_has_phone_number(self):
        self.customer.set_phone_number("09012958377")
        self.assertEqual("09012958377", self.customer.get_phone_number())

    def test_that_customer_can_register(self):
        self.platform.register("titobiloluwa", "Ligali", "titobiloluwaligali2005@gmail.com", "1234", "09012958377")
        self.assertTrue(
            self.platform.register("titobiloluwa", "Ligali", "titobiloluwaligali2005@gmail.com", "1234", "09012958377"))

    def test_that_customer_cannot_register_without_details_being_complete(self):
        self.assertRaises(IncompleteDetails,
                          self.platform.register,"", "Ligali", "titobiloluwaligali2005@gmail.com", "1234",
                                                 "09012958377")


if __name__ == '__main__':
    unittest.main()