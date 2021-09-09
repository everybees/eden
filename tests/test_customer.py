import unittest

from models.customer import Customer
from models.user import User


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_customer_properties(self):
        customer: User = Customer("Ehis", "Edemakhiota", "EdemaEhi17.", "edemaehiz@gmail.com", "ehizman")
        self.assertEqual("Ehis", customer.get__first_name)
        self.assertEqual("Edemakhiota", customer.get__last_name)
        self.assertEqual("EdemaEhi17.", customer.get__password)
        self.assertEqual("edemaehiz@gmail.com", customer.get__email)
        self.assertEqual("ehizman", customer.get__user_name)


if __name__ == '__main__':
    unittest.main()
