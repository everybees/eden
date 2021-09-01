from models.item import Item
from models.product import Product
from models.shopping_cart import Shopping_Cart
from views.product_database_functions import find_product_by_id


def serialize_item_object(item: Item) -> dict:
    return {
        "quantity": item.get__quantity,
        "product": item.get__product_id
    }


def serialize_shopping_cart_object_to_list(cart: Shopping_Cart) -> list:
    list_of_item_dicts: list = []
    if len(cart.get__list_of_items_in_shopping_cart) == 0:
        return list_of_item_dicts
    for item in cart.get__list_of_items_in_shopping_cart:
        list_of_item_dicts.append(serialize_item_object(item))
    return list_of_item_dicts


def deserialize_item_object(item: dict) -> Item:
    quantity: int = item.get("quantity")
    product_id: str = item.get("product")
    product: Product = find_product_by_id(product_id)
    item: Item = Item(quantity=quantity, product=product)
    return item


def deserialize_shopping_cart_object_from_list(cart_as_list: list) -> list:
    list_of_item_objects: list = []
    for item in cart_as_list:
        list_of_item_objects.append(deserialize_item_object(item))
    return list_of_item_objects
