from src.models.user import User


class Customer(User):
    def __init__(self, first_name, last_name, email, user_name, password):
        super().__init__(first_name, last_name, email, user_name, password)
