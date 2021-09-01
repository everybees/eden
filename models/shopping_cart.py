from typing import List

from models.item import Item


class Shopping_Cart:
    def __init__(self):
        self.__list_of_items: List[Item] = list()

    @property
    def get__list_of_items_in_shopping_cart(self):
        return self.__list_of_items

    def add_items_to_shopping_cart(self, *items):
        self.__list_of_items.extend(items)

    def add(self, item):
        self.__list_of_items.append(item)
