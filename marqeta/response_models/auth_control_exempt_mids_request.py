from datetime import datetime, date
from marqeta.response_models.spend_control_association import SpendControlAssociation
import json


class AuthControlExemptMidsRequest(object):

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
    def name(self):

        return self.json_response.get('name', None)

    @property
    def association(self):
        if 'association' in self.json_response:
            return SpendControlAssociation(self.json_response['association'])

    @property
    def mid(self):
        return self.json_response.get('mid', None)

    @property
    def start_time(self):
        if 'start_time' in self.json_response:
            return datetime.strptime(self.json_response['start_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def end_time(self):
        if 'end_time' in self.json_response:
            return datetime.strptime(self.json_response['end_time'], '%Y-%m-%dT%H:%M:%SZ')

    def __repr__(self):
        return '<Marqeta.response_models.auth_control_exempt_mids_request.AuthControlExemptMidsRequest>' + self.__str__()
