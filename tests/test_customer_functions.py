from unittest import TestCase

from models.user_dto import User_Dto
from views.customer_functions import register_customer


class Test(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.file_handler = open("../database/users.json", 'r+', encoding='utf-8')

    def test_register_function(self):
        first_name: str = "Ehis"
        last_name: str = "Edemakhiota"
        email: str = "edemaehiz5.@gmail.com"
        password: str = "EdemaEhi17."
        user_name: str = "ehizman"
        user_dto: User_Dto = register_customer(first_name, last_name, email, password, user_name)
        self.assertEqual("Ehis", user_dto.get__first_name)
