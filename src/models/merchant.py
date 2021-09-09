from models.user import User


class Merchant(User):
    def __init__(self, first_name, last_name, email, user_name, password):
        super(Merchant, self).__init__(first_name, last_name, email, user_name, password)
        self.__list_of_products = []

    @property
    def get__list_of_products(self):
        return self.__list_of_products

    def add_to__list_of_products(self, product):
        return self.__list_of_products.append(product)
