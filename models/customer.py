from dataclasses import dataclass

from models.user import User


class Customer(User):
    def __init__(self, first_name: str, last_name: str, user_name: str, email: str, password: str):
        super(Customer, self).__init__(first_name, last_name, user_name, email, password)

    # def __str__(self):
    #     return f"'Firstname' : {self.get__first_name},"
