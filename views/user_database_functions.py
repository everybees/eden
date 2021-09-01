import json
from typing import Optional

from exceptions.user_exception import UserException
from models.address import Address
from models.billing_info import Billing_Info
from models.credit_card_info import Credit_Card_Info
from models.registration_dto import Registration_Dto
from models.user import User
from views.shopping_cart_functions import serialize_shopping_cart_object_to_list


def deserialize_user_dictionary_to_user_object(user_as_dict: dict) -> User:
    first_name: str = user_as_dict.get("first_name")
    last_name: str = user_as_dict.get("last_name")
    email: str = user_as_dict.get("email")
    password: str = user_as_dict.get("password")
    user: User = User(firstname=first_name, lastname=last_name, email=email, password=password)
    return user


def serialize_address(address: Address):
    return {
        "house_number": address.get__house_number,
        "street": address.get__street_name,
        "city": address.get__city_name,
        "state": address.get__state_name,
        "country": address.get__country_name
    }


def serialize_card_info(card_info: Credit_Card_Info):
    return {
        "name_on_card": card_info.get__name_on_card,
        "card_number": card_info.get__credit_card_number,
        "card_type": card_info.get__card_type,
        "card_cvv": card_info.get__card_cvv,
        "card_expiry_year_month": card_info.get__card_expr_year_month
    }


def deserialize_card_info_to_object(card_info_as_dict: dict) -> Credit_Card_Info:
    name_on_card: str = card_info_as_dict.get("name_on_card")
    card_number: str = card_info_as_dict.get("card_number")
    card_type: str = card_info_as_dict.get("card_type")
    card_cvv: int = card_info_as_dict.get("card_cvv")
    card_expiry_year_month: str = card_info_as_dict.get("card_expiry_year_month")

    credit_card_info: Credit_Card_Info = Credit_Card_Info(name_on_card=name_on_card, credit_card_number=card_number,
                                                          card_type=card_type, cvv=card_cvv,
                                                          expr_year_month=card_expiry_year_month)
    return credit_card_info


def serialize_billing_info(billing_info: Billing_Info):
    return {
        "receiver_first_name": billing_info.get__receiver_first_name(),
        "receiver_last_name": billing_info.get__receiver_last_name(),
        "receiver_phone_number": billing_info.get__receiver_phone_number(),
        "receiver_delivery_address": serialize_address(billing_info.get_delivery_address()),
        "card_info": serialize_card_info(billing_info.get_card_info())
    }


def serialize_customer_object_to_dictionary(customer) -> dict:
    return {"first_name": customer.get__firstname,
            "last_name": customer.get__lastname,
            "email": customer.get__email,
            "password": customer.get__password,
            "is_online": customer.is_online,
            "address": serialize_address(customer.get__home_address),
            "billing_info": {index: serialize_billing_info(billing_info) for index, billing_info in enumerate(customer.get__list_of_billing_info)},
            "cart": serialize_shopping_cart_object_to_list(customer.get__shopping_cart)
            }


def serialize_registration_form_to_user_object(user_to_onboard: Registration_Dto) -> User:
    user: User = User(firstname=user_to_onboard.get__firstname,
                      lastname=user_to_onboard.get__lastname,
                      email=user_to_onboard.get__email,
                      password=user_to_onboard.get__password)
    return user


def save_new_customer_to_database(user) -> None:
    if find_user_in_database_by_email(user.get__email) is not None:
        raise UserException("account already exists!")

    user_details = serialize_customer_object_to_dictionary(user)

    with open("../database/users.json", mode='r', encoding='utf-8') as file_reader:
        file_reader.seek(0)
        json_data: dict = json.load(file_reader)
        json_data["customers"].append(user_details)

    with open("../database/users.json", mode='w', encoding='utf-8') as file_reader:
        json.dump(json_data, file_reader, indent=4)


def find_user_in_database_by_email(email: str) -> Optional[User]:
    with open("../database/users.json", 'r', encoding='utf-8') as file_reader:
        user_as_dict: dict = json.load(file_reader)
        list_of_customer: list = user_as_dict.get("customers")
        for user_customer in list_of_customer:
            if user_customer.get("email") == email:
                user: User = deserialize_user_dictionary_to_user_object(user_customer)
                return user
        return None
