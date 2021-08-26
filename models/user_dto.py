
from models.user import User


class User_Dto(User):

    def __init__(self, first_name="", last_name="", email="", user_name="", password=""):
        super().__init__(first_name, last_name, email, user_name, password)

