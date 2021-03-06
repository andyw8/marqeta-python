from datetime import datetime, date
from marqeta.response_models.funding_source_model import FundingSourceModel
import json


class BankAccountFundingSourceModel(FundingSourceModel):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def user_token(self):
        return self.json_response.get('user_token', None)

    @property
    def business_token(self):
        return self.json_response.get('business_token', None)

    @property
    def account_suffix(self):
        return self.json_response.get('account_suffix', None)

    @property
    def account_type(self):
        return self.json_response.get('account_type', None)

    @property
    def name_on_account(self):
        return self.json_response.get('name_on_account', None)

    @property
    def routing_number(self):
        return self.json_response.get('routing_number', None)

    @property
    def verification_status(self):
        return self.json_response.get('verification_status', None)

    def __repr__(self):
        return '<Marqeta.response_models.bank_account_funding_source_model.BankAccountFundingSourceModel>'\
               + self.__str__()
