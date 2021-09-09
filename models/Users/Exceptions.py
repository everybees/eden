class IncompleteDetails(Exception):
    def __init__(self, message):
        super(IncompleteDetails, self).__init__(message)


class InvalidCustomer(Exception):
    def __init__(self, message):
        super(InvalidCustomer, self).__init__(message)


class InvalidLoginDetails(Exception):
    def __init__(self, message):
        super(InvalidLoginDetails, self).__init__(message)


class UserExists(Exception):
    def __init__(self, message):
        super(UserExists, self).__init__(message)


class ProductExists(Exception):
    def __init__(self, message):
        super(ProductExists, self).__init__(message)

