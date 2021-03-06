from datetime import datetime, date
import json


class NetworkFeeModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def type(self):
        return self.json_response.get('type', None)

    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def credit_debit(self):
        return self.json_response.get('credit_debit', None)

    def __repr__(self):
        return '<Marqeta.response_models.network_fee_model.NetworkFeeModel>' + self.__str__()
