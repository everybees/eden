from unittest import TestCase

from exceptions.user_exception import UserException
from models.customer import Customer
from models.registration_dto import Registration_Dto
from models.user import User
from views.user_database_functions import save_new_user_to_database
from views.user_database_functions import find_user_in_database_by_email


class Test(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.file_handler = open("../database/users.json", 'r+', encoding='utf-8')

    def test_can_save_user_to_database(self):
        user_to_onboard: Registration_Dto = Registration_Dto(first_name="Ehis", last_name="Edemakhiota",
                                                             email="edemaehi4774774@gmail.com",
                                                             password="password", username="ehizman")
        user: User = Customer(Registration_Dto)
        save_new_user_to_database(user_to_onboard)
        found_user: User = find_user_in_database_by_email("edemaehi@gmail.com")
        self.assertEqual(user_to_onboard.get__first_name, found_user.get__first_name)
        self.file_handler.close()

    def test_that_user_cannot_register_twice(self):
        user_to_onboard: Registration_Dto = Registration_Dto(first_name="Ehis", last_name="Edemakhiota",
                                                             email="edemaehi4774774@gmail.com",
                                                             password="password", username="ehizman")
        save_new_user_to_database(user_to_onboard)
        with self.assertRaises(UserException):
            save_new_user_to_database(user_to_onboard)
        self.file_handler.close()
