from typing import Optional
from unittest import TestCase

from exceptions.user_exception import UserException
from models.customer import Customer
from models.registration_dto import Registration_Dto
from models.user_dto import User_Dto
from views.user_database_functions import save_new_customer_to_database
from views.user_database_functions import find_user_in_database_by_email


class Test(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.file_handler = open("../database/users.json", 'r+', encoding='utf-8')

    def test_can_save_user_to_database(self):
        user_to_onboard: Registration_Dto = Registration_Dto(firstname="Ehis", lastname="Edemakhiota",
                                                             email="edemaehi@gmail.com",
                                                             password="password")
        user: Customer = Customer(user_to_onboard)
        save_new_customer_to_database(user)
        optional_found_user: Optional[User_Dto] = find_user_in_database_by_email("edemaehi@gmail.com")
        found_user: User_Dto = optional_found_user
        self.assertIsNotNone(found_user)
        self.assertEqual(user_to_onboard.get__firstname, found_user.get__firstname)
        self.file_handler.close()

    def test_that_user_cannot_register_twice(self):
        user_to_onboard: Registration_Dto = Registration_Dto(firstname="Ehis", lastname="Edemakhiota",
                                                             email="edemaehi4774774@gmail.com",
                                                             password="password")
        user: Customer = Customer(user_to_onboard)
        save_new_customer_to_database(user)
        with self.assertRaises(UserException):
            save_new_customer_to_database(user)
        self.file_handler.close()
