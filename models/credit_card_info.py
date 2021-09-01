from datetime import datetime

from exceptions.invalid_card_exception import Invalid_Card_Exception
from models.card_type import Card_Type


class Credit_Card_Info:
    def __init__(self, cvv: int, expr_year_month: str, credit_card_number: str,
                 name_on_card: str, card_type: str):
        self.__cvv: int = cvv
        self.__expr_year_month: str = expr_year_month
        self.__credit_card_number: str = credit_card_number
        self.__name_on_card: str = name_on_card
        if card_type.lower() == "master card":
            self.__card_type = Card_Type.MASTER_CARD
        elif card_type.lower() == "visa card":
            self.__card_type = Card_Type.VISA_CARD
        elif card_type.lower() == "verve":
            self.__card_type = Card_Type.VERVE
        elif card_type.lower() == "american express":
            self.__card_type = Card_Type.AMERICA_EXPRESS
        else:
            raise Invalid_Card_Exception("Invalid card type")

    @property
    def get__card_cvv(self):
        return self.__cvv

    @property
    def get__card_expr_year_month(self):
        return self.__expr_year_month

    @property
    def get__credit_card_number(self):
        return self.__credit_card_number

    @property
    def get__name_on_card(self):
        return self.__name_on_card

    @property
    def get__card_type(self):
        return self.__card_type