import unittest

from models.Users.Customer import Customer
<<<<<<< Updated upstream
from models.Users.Exceptions import IncompleteDetails, InvalidCustomer
<<<<<<< HEAD
=======
from models.Users.Exceptions import IncompleteDetails
from models.Users.Merchants import Merchant
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
from models.Users.Platfom import Platform
=======
>>>>>>> 68fea1bc1e1f0820aaa6344d7438a8870d138ebf
from models.Users.Users import User


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def setUp(self):
        self.user = User()
        self.customer = Customer("Titobi", "Ligali", "1234", "titobiloluwaligali2005@gmail.com", "09012958377")
<<<<<<< HEAD
        self.merchant = Merchant("", "", "", "", "")
        self.platform = Platform()
=======
>>>>>>> 68fea1bc1e1f0820aaa6344d7438a8870d138ebf

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
        self.assertTrue(
            self.customer.register("titobiloluwa", "Ligali", "titobiloluwaligali2005@gmail.com", "1234", "09012958377"))

    def test_that_customer_cannot_register_without_details_being_complete(self):
        self.assertRaises(IncompleteDetails,
                          self.customer.register, "", "Ligali", "titobiloluwaligali2005@gmail.com", "1234",
                          "09012958377")

<<<<<<< Updated upstream
    def test_that_customer_can_login(self):
        self.customer.register("titobiloluwa", "Ligali", "titobiloluwaligali2005@gmail.com", "1234", "09012958377")
        self.assertTrue(self.customer.login("titobiloluwaligali2005@gmail.com", "1234"))

    def test_that_customer_cannot_login_with_wrong_email(self):
        self.customer.register("titobiloluwa", "Ligali", "titobiloluwaligali2005@gmail.com", "1234", "09012958377")
        self.assertRaises(InvalidCustomer, self.customer.login, "@gmail.com", "1234")

    def test_that_customer_cannot_login_with_wrong_password(self):
        self.customer.register("titobiloluwa", "Ligali", "titobiloluwaligali2005@gmail.com", "1234", "09012958377")
        self.assertRaises(InvalidCustomer, self.customer.login, "titobiloluwaligali2005@gmail.com", "12345")

    def test_for_registered_customers(self):
        self.customer.register("titobiloluwa", "Ligali", "titobiloluwaligali2005@gmail.com", "1234", "09012958377")
        self.assertEqual(1, self.customer.get_number_of_registered_customer())
    #
    # def test_that_customer_can_add_to_cart(self):
    #     self.platform.add_to_cart()

<<<<<<< Updated upstream

<<<<<<< HEAD
    def test_that_customer_can_add_to_cart(self):
        self.platform.add_to_cart()
=======
    def test_that_merchant_can_register(self):
        self.assertEqual(1, self.merchant.register("oja", "sale121", "ojasales@email.com", "+23481123456"))
>>>>>>> Stashed changes
=======
    def test_that_merchant_can_register(self):
        self.assertEqual(1, self.merchant.register("oja", "sale121", "ojasales@email.com", "+23481123456"))
>>>>>>> Stashed changes
=======
>>>>>>> 68fea1bc1e1f0820aaa6344d7438a8870d138ebf
if __name__ == '__main__':
    unittest.main()
