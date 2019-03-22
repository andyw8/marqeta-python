from datetime import datetime, date
from marqeta.response_models.funding_source_model import FundingSourceModel
import json

class ProgramFundingSourceModel(FundingSourceModel):

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
        if 'name' in self.json_response:
            return self.json_response['name']

    def __repr__(self):
         return '<Marqeta.response_models.program_funding_source_model.ProgramFundingSourceModel>'