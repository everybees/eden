import unittest

from models.Merchant import Merchant
from models.Shop import Shop


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.merchant = Merchant("Oluwatobi", "Jolayemi", "jolayemi.tobi@gmail.com", "1234", "08166853770")

    def test_that_merchant_can_create_shop(self):
        self.merchant.create_shop(shop_name="Inclutab")
        self.assertIsInstance(self.merchant.get_shop(), Shop)

    def test_that_merchant_can_add_product_to_shop(self):
        self.merchant.create_shop(shop_name="Inclutab")
        product_name = "Sharp Tv"
        product_description = """
        This is the best TV for small families
        """
        product_price = 20000.00
        product_category = "Electrical Appliances"
        shop_id = "Shoprite"
        self.merchant.create_new_product(product_name, product_description, product_price, product_category, shop_id)
        self.assertIsInstance(self.merchant.get_shop().getProduct())


if __name__ == '__main__':
    unittest.main()
