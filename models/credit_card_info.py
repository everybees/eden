from datetime import datetime

from models.card import Card


class Credit_Card_Info:
    def __init__(self, cvv: int, expr_year_month: datetime, credit_card_number: str,
                 name_on_card: str, card_type: Card):
        self.__cvv: int = cvv
        self.__expr_year_month: str = f"{expr_year_month.year}-{expr_year_month.month}"
        self.__credit_card_number: str = credit_card_number
        self.__name_on_card: str = name_on_card
        self.__card_type = card_type

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
