from datetime import datetime, date
import json

class UserValidationResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def birth_date(self):
        if 'birth_date' in self.json_response:
            return self.json_response['birth_date']

    @property
    def phone(self):
        if 'phone' in self.json_response:
            return self.json_response['phone']

    @property
    def ssn(self):
        if 'ssn' in self.json_response:
            return self.json_response['ssn']

    def __repr__(self):
         return '<Marqeta.response_models.user_validation_response.UserValidationResponse>'