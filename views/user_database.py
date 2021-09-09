import json
from typing import Optional

from exceptions.user_exception import UserException
from models.user import User


def convert_from_user_dictionary_to_user_object(user_as_dict):
    first_name: str = user_as_dict.get("Firstname")
    last_name: str = user_as_dict.get("Lastname")
    email: str = user_as_dict.get("Email")
    username: str = user_as_dict.get("Username")
    password: str = user_as_dict.get("Password")
    user: User = User(first_name, last_name, email, username, password)
    return user


def save_new_user_to_database(customer: User):
    user: User = find_user_in_database_by_email(customer.get__email)

    if user is not None:
        raise UserException("account already exists")

    with open("../database/users.json", 'a', encoding='utf-8') as file_writer:
        user_details: dict = \
            {"Firstname": customer.get__first_name,
             "Lastname": customer.get__last_name,
             "Email": customer.get__email,
             "Username": customer.get__user_name,
             "Password": customer.get__password
             }
        file_writer.seek(1)
        json.dump(user_details, file_writer)
        file_writer.write("\n")


def find_user_in_database_by_email(email: str) -> Optional[User]:
    with open("../database/users.json", 'r', encoding='utf-8') as file_reader:

        for line in file_reader:
            user_as_dict: dict = json.loads(line)
            if user_as_dict.get('Email') == email:
                user: User = convert_from_user_dictionary_to_user_object(user_as_dict)
                return user
        return None
