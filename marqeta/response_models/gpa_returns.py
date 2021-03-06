from datetime import datetime, date
from marqeta.response_models.response import Response
from marqeta.response_models.funding import Funding
import json


class GpaReturns(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        return self.json_response.get('token', None)

    @property
    def amount(self):
        return self.json_response.get('amount', None)

    @property
    def tags(self):
        return self.json_response.get('tags', None)

    @property
    def memo(self):
        return self.json_response.get('memo', None)

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def transaction_token(self):
        return self.json_response.get('transaction_token', None)

    @property
    def state(self):
        return self.json_response.get('state', None)

    @property
    def response(self):
        if 'response' in self.json_response:
            return Response(self.json_response['response'])

    @property
    def funding(self):
        if 'funding' in self.json_response:
            return Funding(self.json_response['funding'])

    @property
    def funding_source_token(self):
        return self.json_response.get('funding_source_token', None)

    @property
    def funding_source_address_token(self):
        return self.json_response.get('funding_source_address_token', None)

    @property
    def original_order_token(self):
        return self.json_response.get('original_order_token', None)

    def __repr__(self):
        return '<Marqeta.response_models.gpa_returns.GpaReturns>' + self.__str__()
