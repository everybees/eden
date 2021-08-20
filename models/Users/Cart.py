import datetime

class Cart:
    def __init__(self, items):
        self.items = items
        self.date = datetime.datetime.now()
