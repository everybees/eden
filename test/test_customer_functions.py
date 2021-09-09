import unittest

from exceptions.login_exception import Login_Exception
from models.item import Item
from models.product import Product
from models.product_category import Product_Category
from views.user_database import find_customer_by_email, save_customer, serialize_item
from views.user_function import login


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_user_can_login(self):
        result = login("edemaehiz@yahoo.com", "EdemaEhi17.")
        self.assertTrue(result)

    def test_user_cannot_login_with_invalid_email(self):
        with self.assertRaises(Login_Exception):
            login("edemaehiz@gmail.com", "EdemaEhi17.")

    def test_user_cannot_login_with_invalid_password(self):
        with self.assertRaises(Login_Exception):
            login("edemaehiz@yahoo.com", "EdemaEhi.")

    def test_user_can_add_item_to_cart(self):
        found_user = find_customer_by_email("edemaehiz@yahoo.com")
        product = Product(name="Corn Flakes", product_desc="bathing soap", price=50,
                          category=Product_Category.GROCERIES)
        item = Item(quantity=24, product=product)
        found_user.get__cart.add_item_to_cart(item=item)
        save_customer(found_user)



if __name__ == '__main__':
    unittest.main()
