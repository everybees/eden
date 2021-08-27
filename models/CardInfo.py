class CardInfo():
    def __init__(self, card_number, cvv, expiration_date, card_type):
        self.__card_number = card_number
        self.__cvv = cvv
        self.__expiration_date = expiration_date
        self.card_type = card_type
