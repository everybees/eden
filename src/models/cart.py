class Cart:
    def __init__(self):
        self.__list_of_items = []

    def add_item_to_cart(self, item):
        self.__list_of_items.append(item)

    def get_items_in_cart(self):
        return self.__list_of_items
