class InvalidUserException(Exception):
    def __init__(self):
        super().__init__("Invalid User")


class CardDoesNotExistException(Exception):
    def __init__(self):
        super().__init__('Card type does not exist')


class InvalidAddressException(Exception):
    def __init__(self):
        super().__init__('Address does not match')


class InvalidCardException(Exception):
    def __init__(self):
        super().__init__("Please provide correct card details")


class CategoryNotFoundException(Exception):
    def __init__(self):
        super().__init__("This category is currently not available")
