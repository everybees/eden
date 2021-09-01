from typing import Optional

from exceptions.invalid_operation_exception import Invalid_Operation_Exception
from exceptions.user_exception import UserException
from models.user import User
from models.user_dto import User_Dto
from views.dashboard_functions import display_dashboard
from views.user_database_functions import save_new_customer_to_database, find_user_in_database_by_email


def register_customer(customer) -> User_Dto:
    # if registration_dto is None:
    #     raise RegistrationException("No user details provided")
    # if registration_dto.get__firstname.strip() == "" or registration_dto.get__lastname.strip() == "" or registration_dto.get__email.strip() == "" or registration_dto.get__password.strip() == "":
    #     raise RegistrationException("No user details provided")

    # customer: Customer = Customer(registration_dto=registration_dto)
    save_new_customer_to_database(customer)
    user_dto: User_Dto = User_Dto(firstname=customer.get__firstname,
                                  lastname=customer.get__lastname, email=customer.get__email)
    return user_dto


def update_customer(user_details_update, email: str):
    if user_details_update is None:
        raise UserException("invalid parameters provided for update")
    elif (user_details_update.get__firstname == '') and (user_details_update.get__lastname == '') and (
            user_details_update.get__email == '') and (user_details_update.get__password == ''):
        raise UserException("invalid parameters provided for update")
    user_to_update = find_user_in_database_by_email(email=email)
    if user_to_update is None:
        raise UserException("No matching details found in database")
    else:
        if user_details_update.get__firstname != '':
            user_to_update.update_firstname(user_details_update.get__firstname)
        if user_details_update.get__lastname != '':
            user_to_update.update__lastname(user_details_update.get__lastname)
        if user_details_update.get__email != '':
            user_to_update.update__email(user_details_update.get__email)
        if user_details_update.get__password != '':
            user_to_update.update__password(user_details_update.get__password)


def login(email: str, password: str) -> User_Dto:
    user = find_user_in_database_by_email(email)
    if user is None:
        raise UserException("invalid email")
    if user.is_online:
        raise Invalid_Operation_Exception("user cannot login when logged in already")
    if user.get__password == password:
        raise UserException("invalid password")
    else:
        user.set__is_online()
        update_customer(user, email)
        display_dashboard(user)
        user_dto: User_Dto = User_Dto(firstname=user.get__firstname,
                            lastname=user.get__lastname,
                            email=user.get__email)
        return user_dto


def logout(email: str):
    user: User = find_user_in_database_by_email(email=email)
    if not user.is_online:
        raise Invalid_Operation_Exception("user cannot logout when already logged out")
    user.set__is_online()
