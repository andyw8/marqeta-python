from datetime import datetime, date
import json


class SpendControlAssociation(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def card_product_token(self):
        return self.json_response.get('card_product_token', None)

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    def __repr__(self):
        return '<Marqeta.response_models.spend_control_association.SpendControlAssociation>' + self.__str__()
