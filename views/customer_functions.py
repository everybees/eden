from models.customer import Customer
from models.registration_dto import Registration_Dto
from models.user import User
from models.user_dto import User_Dto
from views.user_database_functions import save_new_user_to_database


def register_customer(registration_dto: Registration_Dto) -> User_Dto:
    customer: User = Customer(registration_dto.get__first_name, registration_dto.get__last_name,
                              registration_dto.get__email, registration_dto.get__user_name,
                              registration_dto.get__password)
    save_new_user_to_database(customer)
    user_dto: User_Dto = User_Dto()
    user_dto.update_first_name(customer.get__first_name)
    user_dto.update__last_name(customer.get__last_name)
    user_dto.update_user_name(customer.get__user_name)
    user_dto.update__password(customer.get__password)
    user_dto.update__email(customer.get__email)
    return user_dto
