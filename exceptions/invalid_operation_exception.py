from exceptions.eden_exception import Eden_Exception


class Invalid_Operation_Exception(Eden_Exception):
    def __init__(self, message):
        super(Invalid_Operation_Exception, self).__init__(message)