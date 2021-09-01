import unittest

from models.address import Address
from models.billing_info import Billing_Info
from models.credit_card_info import Credit_Card_Info
from models.customer import Customer
from models.registration_dto import Registration_Dto


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.file_handler = open("../database/users.json", 'r+', encoding='utf-8')

    def test_something(self):
        self.assertEqual(True, True)

    def test_customer_properties(self):
        registration_dto: Registration_Dto = Registration_Dto(firstname="Ehis", lastname="Edemakhiota",
                                                              email="edemaehi@gmail.com",
                                                              password="EdemaEhi17.")
        customer: Customer = Customer(registration_dto)
        self.assertEqual("Ehis", customer.get__firstname)
        self.assertEqual("Edemakhiota", customer.get__lastname)
        self.assertEqual("EdemaEhi17.", customer.get__password)
        self.assertEqual("edemaehi@gmail.com", customer.get__email)

    def test_that_customer_has_a_list_of_Billing_information(self):
        registration_dto: Registration_Dto = Registration_Dto(firstname="Ehis", lastname="Edemakhiota",
                                                              email="edemaehi@gmail.com",
                                                              password="__password")
        customer: Customer = Customer(registration_dto)
        self.assertListEqual([], customer.get__list_of_billing_info)

    def test_that_user_can_add_an_address_to_list_of_Billing_information(self):
        registration_dto: Registration_Dto = Registration_Dto(firstname="Ehis", lastname="Edemakhiota",
                                                              email="edemaeseosa@gmail.com",
                                                              password="EdemaEhi17.")

        customer: Customer = Customer(registration_dto)
        address: Address = Address(house_number=312,
                                   street_name="Hebert Macaulay Way",
                                   city_name="Sabo- Yaba",
                                   state_name="Lagos",
                                   country_name="Nigeria")
        credit_card_info: Credit_Card_Info = Credit_Card_Info(card_type="master card",
                                                              name_on_card="Ehis Edemakhiota", cvv=567,
                                                              expr_year_month="2021-09",
                                                              credit_card_number="2345648746476")
        new_billing_info: Billing_Info = Billing_Info(receiver_first_name="Ehis", receiver_last_name="Edemakhiota",
                                                      receiver_phone_number="+2348134922538", delivery_address=address,
                                                      credit_card_info=credit_card_info)
        customer.update__list_of_billing_info(new_billing_info=new_billing_info)
        self.assertEqual(1, len(customer.get__list_of_billing_info))


if __name__ == '__main__':
    unittest.main()
