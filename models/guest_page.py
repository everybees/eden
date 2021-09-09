from views.logout import logout
from views.cart_function import add_to_cart
from views.login import login_as_customer, login_as_admin
from views.login import login_as_merchant

if __name__ == '__main__':
    message = """
    Welcome to Evolve Store:
    -> Press 1 to view products
    -> Press 2 to signup(as a customer)
    -> Press 3 to signup(as a merchant)
    -> Press 4 to login(as a customer)
    -> Press 5 to login(as a merchant)
    -> Press 6 to login(ADMINISTRATOR ONLY)
    """

    user_input = int(input(message))

    if user_input == 1:
        message_two = """
        press 1 for Banana
        press 2 for Gun
        press 3 for Salt
        press 4 for Sunshades
        """

        user_input_two = int(input(message_two))

        if user_input_two == 1:
            quantity = int(input("how many?:"))
            add_to_cart("Banana", quantity, 30)

            order = input("press ok to place your order: ")

            if order == 'ok':
                print("You have to register to place your order")
                first_name = input("Enter your first name")
                last_name = input("Enter your last name")
                email = input("Enter your email")
                password = input("Enter your password")
                print(first_name, last_name, email)

        elif user_input == 2:
            quantity = int(input("how many?:"))
            add_to_cart("Gun", quantity, 500)

            order_two = input("press ok to place your order: ")

            if order_two == 'ok':
                print("You have to register to place your order")
                first_name = input("Enter your first name")
                last_name = input("Enter your last name")
                email = input("Enter your email")
                password = input("Enter your password")
                print(first_name, last_name, email)

    if user_input == 2:
        print("Register below")
        first_name = input("Enter your first name")
        last_name = input("Enter your last name")
        email = input("Enter your email")
        password = input("Enter your password")
        print(first_name, last_name, email)

    if user_input == 3:
        print("Register below")
        first_name = input("Enter your first name")
        last_name = input("Enter your last name")
        email = input("Enter your email")
        password = input("Enter your password")
        print(first_name, last_name, email)

    if user_input == 4:
        email = input("Enter your email")
        password = input("Enter your password")
        login_as_customer(email, password)

    if user_input == 5:
        email = input("Enter your email")
        password = input("Enter your password")
        login_as_merchant(email, password)

    if user_input == 5:
        password = input("Enter your password")
        login_as_admin(password)

