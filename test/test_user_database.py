from unittest import TestCase

from models.user import User
from views.user_database import find_user_by_email
from views.user_function import register_user


class TestUser_Database(TestCase):
    def test_save_user(self):
        register_user(first_name="Ehimwenman", last_name="Edemakhiota", user_name="ehizman",
                      password="EdemaEhi17.", email="edemaehiz@yahoo.com")
        result = find_user_by_email("edemaehiz@yahoo.com")
        self.assertTrue(result)
        self.assertFalse(find_user_by_email("edemaehiz@gmail.com"))
