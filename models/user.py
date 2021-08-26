from exception.exception import InvalidUserException, CardDoesNotExistException, InvalidAddressException, \
    InvalidCardException
from models import enum_types
from models.enum_types import UserType


class User:
    def __init__(self, first_name='', last_name='', email='', password='', type_of_user=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        if type(type_of_user) is enum_types.UserType:
            self.type_of_user = type_of_user
        else:
            raise InvalidUserException()


class Address:
    def __init__(self, number=0, street_name='', town='', state=''):
        self.number = number
        self.street_name = street_name
        self.town = town
        self.state = state


class CardDetails:
    def __init__(self, name='', card_type= None, card_number='', pin=0):
        self.name = name
        if type(card_type) is enum_types.CardType:
            self.card_type = card_type
        else:
            raise CardDoesNotExistException()
        self.card_number = card_number
        self.pin = pin


class Customer(User):
    def __init__(self, first_name='', last_name='', email='', password='', type_of_user=None, address='', card_details=None):
        super().__init__(first_name, last_name, email, password, type_of_user)
        if type_of_user != UserType.CUSTOMER:
            raise InvalidUserException()
        else:
            self.type_of_user = type_of_user
        if type(address) is Address:
            self.address = address
        else:
            raise InvalidAddressException()
        if type(card_details) is CardDetails:
            self.card_details = card_details
        else:
            raise InvalidCardException()

