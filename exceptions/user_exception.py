class UserException(Exception):
    def __init__(self, message):
        super(UserException, self).__init__(message)
