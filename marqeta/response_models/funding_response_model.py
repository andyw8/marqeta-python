from datetime import datetime, date
from marqeta.response_models.gatewaylog import Gatewaylog
import json

class FundingResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def id(self):
        if 'id' in self.json_response:
            return self.json_response['id']

    @property
    def accounting_balance(self):
        if 'accounting_balance' in self.json_response:
            return self.json_response['accounting_balance']

    @property
    def available_balance(self):
        if 'available_balance' in self.json_response:
            return self.json_response['available_balance']

    @property
    def transaction(self):
        if 'transaction' in self.json_response:
            return Gatewaylog(self.json_response['transaction'])

    def __repr__(self):
         return '<Marqeta.response_models.funding_response_model.FundingResponseModel>'