class IncompleteDetails(Exception):
    def __init__(self, message):
        super(IncompleteDetails, self).__init__(message)


class InvalidCustomer(Exception):
    def __init__(self, message):
        super(InvalidCustomer, self).__init__(message)

