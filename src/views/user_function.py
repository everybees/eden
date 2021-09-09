from models.user import User
from views.user_database import save_user


def register_user(first_name, last_name, email, password, user_name):
    user = User(first_name=first_name, last_name=last_name, password=password,email=email, user_name=user_name)
    save_user(user=user)
