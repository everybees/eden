import unittest
from models.merchant import Merchant


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_merchant_account_log_in(self):

        first_merchant = Merchant("sleakys","TechHub","Kola", "Badmus","badmuskola1989@gmail.com","kola1234")
        self.assertEqual("welcomed back", first_merchant.log_in("kola","kola1989")) #test will fail




if __name__ == '__main__':
    unittest.main()
