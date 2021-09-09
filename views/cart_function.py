general_list = []


def add_to_cart(product_name, quantity, price):
    items = [product_name, quantity, price]

    return items


def all_items(number_of_product):
    for i in range(number_of_product):
        general_list.append(add_to_cart())

    return general_list


def remove_from_cart(index):
    general_list.remove(index)

    return general_list


def place_order():
    total_order = []
    total = 1
    total_pay = 0

    for smaller_list in general_list:
        for index in smaller_list:
            if index == 1 or index == 2:
                total += smaller_list[index]
        total_order.append(total)

    for i in total_order:
        total_pay += total_order[i]

    return total_pay

def cancel_order():
    general_list.clear()
