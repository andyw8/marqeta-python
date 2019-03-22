from datetime import datetime, date
from marqeta.response_models.auto_reload_association import AutoReloadAssociation
from marqeta.response_models.order_scope import OrderScope
import json

class AutoReloadUpdateModel(object):

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
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def funding_source_token(self):
        if 'funding_source_token' in self.json_response:
            return self.json_response['funding_source_token']

    @property
    def funding_source_address_token(self):
        if 'funding_source_address_token' in self.json_response:
            return self.json_response['funding_source_address_token']

    @property
    def association(self):
        if 'association' in self.json_response:
            return AutoReloadAssociation(self.json_response['association'])

    @property
    def order_scope(self):
        if 'order_scope' in self.json_response:
            return OrderScope(self.json_response['order_scope'])

    @property
    def currency_code(self):
        if 'currency_code' in self.json_response:
            return self.json_response['currency_code']

    def __repr__(self):
         return '<Marqeta.response_models.auto_reload_update_model.AutoReloadUpdateModel>'