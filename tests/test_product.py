from unittest import TestCase

from models.product import Product
from models.product_category import Product_Category


class Test(TestCase):
    def test_constructor(self):
        product: Product = Product(product_name="Dettol Soap", price=350.00, product_description="bathing soap for "
                                                                                                 "babies",
                                   product_category="groceries")
        self.assertEqual("Dettol Soap", product.get__product_name)
        self.assertEqual(350.00, product.get__price)
        self.assertEqual("bathing soap for babies", product.get__description)
        self.assertEqual(Product_Category.GROCERIES, product.get__category)
        self.assertIn("SKU", product.get__id)
        print(product.get__id)
