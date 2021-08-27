import unittest
from models.Address import Address
from models.CardInfo import CardInfo
from models.CardType import CardType
from models.Customer import Customer


class MyTestCase(unittest.TestCase):

    def setUp(cls) -> None:
        cls.customer = Customer("Oluwatobi", "Jolayemi", "jolayemi.tobi@gmail.com", "1234", "08166853770")

    def test_customer_have_billing_info(self):
        address = Address("1", "Shodipe street", "Lagos", "Nigeria")
        card_info = CardInfo("5399-4567-3456-0098", "234", "04/25", CardType.CREDITCARD)
        self.customer.set_billing_info(address, card_info)
        self.assertIsNotNone(self.customer.get_billing_info())

    # def test_customer_have_shopping_cart(self):



if __name__ == '__main__':
    unittest.main()
