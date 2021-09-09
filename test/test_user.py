from unittest import TestCase

from src.models.user import User


class TestUser(TestCase):
    pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.user: User = User(first_name="Ehis", last_name="Edemakhiota", user_name="ehizman", password="EdemaEhiz17.",
                              email="edemaehiz@gmail.com")

    def test_get__firstname(self):
        first_name = self.user.get__first_name
        self.assertEqual("Ehis", first_name)

    def test_set__firstname(self):
        self.user.set__first_name(first_name="Mark")
        self.assertEqual("Mark", self.user.get__first_name)

    def test_get__lastname(self):
        last_name = self.user.get__last_name
        self.assertEqual("Edemakhiota", last_name)

    def test_set__lastname(self):
        self.user.set__first_name(first_name="Ikpea")
        self.assertEqual("Ikpea", self.user.get__first_name)

    def test_get__email(self):
        email = self.user.get__email
        self.assertEqual("edemaehiz@gmail.com", email)

    def test_set__email(self):
        self.user.set__email(email="edemaehiz@yahoo.com")
        self.assertEqual("edemaehiz@yahoo.com", self.user.get__email)

    def test_get__password(self):
        password = self.user.get__password
        self.assertEqual("EdemaEhiz17.", password)

    def test_set__password(self):
        self.user.set__password(password="edemaehiz@yahoo.com")
        self.assertEqual("edemaehiz@yahoo.com", self.user.get__password)

    def test_get__user_name(self):
        user_name = self.user.get__user_name
        self.assertEqual("ehizman", user_name)

    def test_set__user_name(self):
        self.user.set__user_name(user_name="the main man")
        self.assertEqual("the main man", self.user.get__user_name)
