# contains admin class
from models.User import user


class Admin(user):
    def __init__(self,firstname, lastname, id, email, password, usertype):
        super().__init__(firstname, lastname, id, email, password, usertype)
