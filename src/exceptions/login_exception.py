class Login_Exception(Exception):
    def __init__(self, message):
        super(Login_Exception, self).__init__(message)