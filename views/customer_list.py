customers = []


def add_customers(customer):
    customers.append(customer)
    return customers


def delete_customers(index):
    customers.remove(index)
    return customers
