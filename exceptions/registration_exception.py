from exceptions.eden_exception import Eden_Exception


class RegistrationException(Eden_Exception):
    def __init__(self, message):
        super(RegistrationException, self).__init__(message)
