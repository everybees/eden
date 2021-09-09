from unittest import TestCase

from exceptions.user_exception import UserException
from models.user import User
from views.user_database import save_new_user_to_database
from views.user_database import find_user_in_database_by_email


class Test(TestCase):
    def test_find_user_in_database_by_email(self):
        self.fail()

    def test_can_save_user_to_database(self):
        user: User = User(first_name="Ehis", last_name="Edemakhiota",
                          email="edemaehiz@gmail.com", user_name="ehizman",
                          password="password")
        save_new_user_to_database(user)
        found_user: User = find_user_in_database_by_email("edemaehiz@gmail.com")
        self.assertEqual(user.get__first_name, found_user.get__first_name)

    def test_that_user_cannot_register_twice(self):
        user: User = User(first_name="Ehis", last_name="Edemakhiota",
                          email="edemaehiz@gmail.com", user_name="ehizman",
                          password="password")
        save_new_user_to_database(user)
        with self.assertRaises(UserException):
            save_new_user_to_database(user)

