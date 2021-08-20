class IncompleteDetails(Exception):
    def __init__(self, message):
        super(IncompleteDetails, self).__init__(message)
