class Cart:
    def __init__(self):
        self.__list_of_items = []

    def add_item_to_cart(self, item):
        in_cart = False
        for stored_item in self.__list_of_items:
            if stored_item.get__product.get__product_name == item.get__product.get__product_name:
                print(item.get__product.get__product_name)
                print(stored_item.get__product.get__product_name)
                in_cart = True
                item.update_product_quantity()
        if not in_cart:
            self.__list_of_items.append(item)

    def get_items_in_cart(self):
        return self.__list_of_items
