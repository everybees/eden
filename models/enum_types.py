import enum


class UserType(enum.Enum):
    ADMIN = 1
    CUSTOMER = 2
    MERCHANT = 3


class CardType(enum.Enum):
    VISA = 1
    VERVE = 2
    MASTERCARD = 3