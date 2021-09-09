from models.Users.Users import User
from models.Users.address import Address
import datetime


class Account:
    user = User
    address = Address

    def __init__(self, user: User, address: Address):
        self.user = user
        self.address = address
        self.opening_date = datetime.datetime.now()
