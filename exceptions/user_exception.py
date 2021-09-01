from exceptions.eden_exception import Eden_Exception


class UserException(Eden_Exception):
    def __init__(self, message):
        super(UserException, self).__init__(message)