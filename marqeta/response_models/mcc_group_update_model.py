from datetime import datetime, date
from marqeta.response_models.config import Config
import json


class MccGroupUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        return self.json_response.get('name', None)

    @property
    def mccs(self):
        return self.json_response.get('mccs', None)

    @property
    def active(self):
        return self.json_response.get('active', None)

    @property
    def config(self):
        if 'config' in self.json_response:
            return Config(self.json_response['config'])

    def __repr__(self):
        return '<Marqeta.response_models.mcc_group_update_model.MccGroupUpdateModel>' + self.__str__()
