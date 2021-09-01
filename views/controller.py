from models.customer import Customer
from models.registration_dto import Registration_Dto
from views.customer_functions import register_customer


def register(registration_dto: Registration_Dto):
    customer: Customer = Customer(registration_dto=registration_dto)
    register_customer(customer=customer)