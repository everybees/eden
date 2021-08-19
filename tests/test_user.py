import unittest

from models.user import User


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_user_constructor(self):
        user = User()
        self.assertIsNotNone(user)


if __name__ == '__main__':
    unittest.main()
