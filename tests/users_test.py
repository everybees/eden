import unittest

from exception.exception import CardDoesNotExistException, InvalidAddressException
from models.enum_types import UserType, CardType
from models.user import User, Address, CardDetails, Customer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_that_user_has_first_name(self):
        user = User('Ifeanyi', 'Osuji', 'oi@gmail.com', '2217', UserType.ADMIN)
        self.assertEqual('Ifeanyi', user.first_name)

    def test_that_user_has_last_name(self):
        user = User('Ifeanyi', 'Osuji', 'oi@gmail.com', '2217', UserType.ADMIN)
        self.assertEqual('Osuji', user.last_name)

    def test_that_user_has_email(self):
        user = User('Ifeanyi', 'Osuji', 'oi@gmail.com', '2217', UserType.CUSTOMER)
        self.assertEqual('oi@gmail.com', user.email)

    def test_that_user_has_password(self):
        user = User('Ifeanyi', 'Osuji', 'oi@gmail.com', '2217', UserType.ADMIN)
        self.assertEqual('2217', user.password)

    def test_that_individual_is_a_user(self):
        user = User('Ifeanyi', 'Osuji', 'oi@gmail.com', '2217', UserType.CUSTOMER)
        self.assertEqual(UserType.CUSTOMER, user.type_of_user)

    def test_that_individual_must_be_of_type_user(self):
        user = User('Ifeanyi', 'Osuji', 'oi@gmail.com', '2217', UserType.ADMIN)
        self.assertEqual(UserType.ADMIN, user.type_of_user)


    def test_that_user_address_has_number(self):
        address = Address(1233)
        self.assertEqual(1233, address.number)

    def test_that_user_address_has_street_number(self):
        address = Address(1233, 'Sabo')
        self.assertEqual('Sabo', address.street_name)

    def test_that_user_address_has_town(self):
        address = Address(1233, 'Sabo', 'Yaba')
        self.assertEqual('Yaba', address.town)

    def test_that_user_address_has_state(self):
        address = Address(1233, 'Sabo', 'Yaba','Lagos')
        self.assertEqual('Lagos', address.state)

    def test_that_user_card_has_name(self):
        card = CardDetails('Ifeanyi Osuji', CardType.VISA)
        self.assertEqual('Ifeanyi Osuji', card.name)

    def test_that_user_card_has_type(self):
        card = CardDetails('Ifeanyi Osuji', CardType.VISA)
        self.assertEqual(CardType.VISA, card.card_type)

    def test_that_user_card_has_number(self):
        card = CardDetails('Ifeanyi Osuji', 'VISA', '123456123')
        self.assertEqual('123456123', card.card_number)

    def test_that_user_card_has_pin(self):
        card = CardDetails('Ifeanyi Osuji', CardType.VISA, '123456123', 1234)
        self.assertEqual(1234, card.pin)

    def test_that_customer_card_is_of_card_type(self):
        self.assertRaises(CardDoesNotExistException, CardDetails, 'VISA')

    def test_that_customer_address_is_of_type_address(self):
        address = Address()
        card = CardDetails( card_type=CardType.VISA)
        customer = Customer(type_of_user=UserType.CUSTOMER, address=address, card_details=card)
        self.assertEqual(address, customer.address)





if __name__ == '__main__':
    unittest.main()
