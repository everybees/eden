from models.Users.Users import User


class Account:
    user = User

    def __init__(self, user):
        self.user = user
