from exceptions.eden_exception import Eden_Exception


class Product_Exception(Eden_Exception):
    def __init__(self, message):
        super(Product_Exception, self).__init__(message=message)
