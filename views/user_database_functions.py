import json
from typing import Optional

from exceptions.user_exception import UserException
from models.registration_dto import Registration_Dto
from models.user import User
from models.user_dto import User_Dto


def convert_from_user_dictionary_to_user_dto_object(user_as_dict) -> User_Dto:
    first_name: str = user_as_dict.get("Firstname")
    last_name: str = user_as_dict.get("Lastname")
    email: str = user_as_dict.get("Email")
    username: str = user_as_dict.get("Username")
    password: str = user_as_dict.get("Password")
    user_dto: User_Dto = User_Dto(first_name, last_name, email, username, password)
    return user_dto


def convert_from_user_object_to_dictionary(customer) -> dict:
    return {"Firstname": customer.get__first_name,
            "Lastname": customer.get__last_name,
            "Email": customer.get__email,
            "Username": customer.get__user_name,
            "Password": customer.get__password
            }


def convert_registration_form_to_user_object(user_to_onboard) -> User:
    user: User = User(first_name=user_to_onboard.get__first_name, last_name=user_to_onboard.get__last_name,
                      email=user_to_onboard.get__email, password=user_to_onboard.get__password,
                      user_name=user_to_onboard.get__user_name)
    return user


def save_new_user_to_database(user: User) -> None:
    if find_user_in_database_by_email(user.get__email) is not None:
        raise UserException("account already exists!")

    user_details = convert_from_user_object_to_dictionary(user)

    with open("../database/users.json", mode='r', encoding='utf-8') as file_reader:
        file_reader.seek(0)
        json_data: dict = json.load(file_reader)
        json_data["customers"].append(user_details)

    with open("../database/users.json", mode='w', encoding='utf-8') as file_reader:
        json.dump(json_data, file_reader, indent=4)


def find_user_in_database_by_email(email: str) -> Optional[User_Dto]:
    with open("../database/users.json", 'r', encoding='utf-8') as file_reader:
        user_as_dict: dict = json.load(file_reader)
        list_of_customer: list = user_as_dict.get("customers")
        for user_customer in list_of_customer:
            if user_customer.get("Email") == email:
                user_object: User_Dto = convert_from_user_dictionary_to_user_dto_object(user_customer)
                return user_object
    return None
