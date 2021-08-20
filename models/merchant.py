# contains merchant class
from models.User import user


class Merchant(user):
        def __init__(self,firstname, lastname, id, email, password, usertype, billing_address, card_details, shop):
            super().__init__(firstname, lastname, id, email, password, usertype)

            self.billing_address = billing_address
            self.card_details = card_details
            self.shop = shop