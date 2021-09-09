from unittest import TestCase

from src.models.customer import Customer


class Test(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.customer: Customer = Customer(first_name="Ehis", last_name="Edemakhiota", user_name="ehizman",
                                          password="EdemaEhi17.", email="edemaehiz@gmail.com")

    def test_get_customer_first_name(self):
        first_name = self.customer.get__first_name
        self.assertEqual("Ehis", first_name)
