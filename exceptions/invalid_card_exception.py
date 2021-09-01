from exceptions.eden_exception import Eden_Exception


class Invalid_Card_Exception(Eden_Exception):
    def __init__(self, message: str):
        super(Invalid_Card_Exception, self).__init__(message)
