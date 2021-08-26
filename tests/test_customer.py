import unittest
from models.user_dto import User_Dto
from views.customer_functions import register_customer


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.file_handler = open("../database/users.json", 'r+', encoding='utf-8')

    def test_something(self):
        self.assertEqual(True, True)

    def test_customer_properties(self):
        customer_dto: User_Dto = register_customer("Ehis", "Edemakhiota", "EdemaEhi17.", "edemaehiz@gmail.com",
                                                   "ehizman")
        self.assertEqual("Ehis", customer_dto.get__first_name)
        self.assertEqual("Edemakhiota", customer_dto.get__last_name)
        self.assertEqual("EdemaEhi17.", customer_dto.get__password)
        self.assertEqual("edemaehiz@gmail.com", customer_dto.get__email)
        self.assertEqual("ehizman", customer_dto.get__user_name)

    def test_that_user_has_a_list_of_Billing_information(self):
        customer_dto: User_Dto = register_customer("Ehis", "Edemakhiota", "EdemaEhi17.", "edemaehiz.@gmail.com",
                                                   "ehizman")
        self.assertListEqual([], customer_dto.get__list_of_billing_info)

    def test_that_user_can_add_an_address_to_list_of_Billing_information(self):
        customer_dto: User_Dto = register_customer("Ehis", "Edemakhiota", "EdemaEhi17.", "edemaehiz@gmail.com",
                                                   "ehizman")


if __name__ == '__main__':
    unittest.main()
