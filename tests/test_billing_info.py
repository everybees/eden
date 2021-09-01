from datetime import datetime
from unittest import TestCase

from models.address import Address
from models.billing_info import Billing_Info
from models.credit_card_info import Credit_Card_Info


class Test(TestCase):
    def test_create_billing_info(self):
        address: Address = Address(house_number=312, street_name="Hebert Macaulay Way",
                                   city_name="Yaba", state_name="Lagos", country_name="Nigeria")
        credit_card_info: Credit_Card_Info = Credit_Card_Info(card_type="master card",
                                                              name_on_card="Ehis Edemakhiota", cvv=567,
                                                              expr_year_month=datetime.now(),
                                                              credit_card_number="2345648746476")

        new_billing_info: Billing_Info = Billing_Info(receiver_first_name="Ehis", receiver_last_name="Edemakhiota",
                                                      receiver_phone_number="+2348134922538", delivery_address=address,
                                                      credit_card_info=credit_card_info)

        self.assertEqual("Ehis", new_billing_info.get__receiver_first_name)
        self.assertEqual("Edemakhiota", new_billing_info.get__receiver_last_name)
        self.assertEqual("+2348134922538", new_billing_info.get__receiver_phone_number)
        self.assertEqual(address, new_billing_info.get_delivery_address)
        self.assertEqual(credit_card_info, new_billing_info.get_card_info)
