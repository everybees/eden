from typing import Optional
from unittest import TestCase

from models.registration_dto import Registration_Dto
from models.user_dto import User_Dto
from views.controller import register
from views.customer_functions import register_customer, login, logout


class Test(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.file_handler = open("../database/users.json", 'r+', encoding='utf-8')

    def test_register_function(self):
        firstname: str = "Ehis"
        lastname: str = "Edemakhiota"
        email: str = "edemaehiz5.@gmail.com"
        password: str = "EdemaEhi17."
        registration_Dto: Registration_Dto = Registration_Dto(firstname=firstname, lastname=lastname, email=email,
                                                              password=password)
        user_dto: User_Dto = register(registration_dto=registration_Dto)
        self.assertEqual("Ehis", user_dto.get__firstname)
        self.file_handler.close()

    def test_login_function(self):
        user_dto: User_Dto = login(email="edemaehiz5.@gmail.com", password="EdemaEhi17.")
        self.assertEqual("Ehis", user_dto.get__firstname)
        self.assertEqual("Edemakhiota", user_dto.get__lastname)
        self.file_handler.close()

    def test_logout_function(self):
        logout("edemaehiz5.@gmail.com")
