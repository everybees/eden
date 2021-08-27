from models.User import User


class Admin(User):
    def __init__(self, first_name, last_name, email_address, password, phone_number):
        super().__init__(first_name, last_name, email_address, password, phone_number)
