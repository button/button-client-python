from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import hashlib

from pybutton.resources.private_audience.model.model import PrivateAudienceModel  # noqa: E501
from pybutton.resources.resource import Resource
from pybutton.error import ButtonClientError


class PrivateAudience(Resource):

    def _validateEnvironment(self, requires_model):
        if not self.config['private_audience_secret']:
            raise ButtonClientError((
                'Your private audience secret must be set in the config as '
                '`private_audience_secret`.'
            ))
        if requires_model:
            try:
                self.private_audience_loaded
            except:
                raise ButtonClientError((
                    'A private audience file has not yet been loaded.'
                ))

    def _cleanAndHashIdentifier(self, identifier):
        try:
            clean_identifier = identifier.encode('utf-8').lower().strip()
            hashed_identifier = hashlib.sha256(clean_identifier)
            hashed_identifier.update(
                self.config['private_audience_secret'].encode('utf-8'))
            return hashed_identifier.hexdigest()
        except:
            return None

    def load(self, filename):
        self._validateEnvironment(False)
        with open(filename, 'rb') as fp:
            self.private_audience_loaded = PrivateAudienceModel.fromfile(fp)
        return 'success'

    def evaluate(self, identifier):
        self._validateEnvironment(True)
        hashed_id = self._cleanAndHashIdentifier(identifier)
        return hashed_id in self.private_audience_loaded

    def match(self, match_list):
        self._validateEnvironment(True)
        return_list = []
        for m in match_list:
            hashed_id = self._cleanAndHashIdentifier(m)
            if hashed_id in self.private_audience_loaded:
                return_list.append(m)
        return return_list

    def create(self, audience_name, identifier_list, error_rt=0.00001):
        self._validateEnvironment(False)
        # Initialize Bloom Filter
        f = PrivateAudienceModel(capacity=len(identifier_list), error_rate=error_rt)  # noqa: E501
        for m in identifier_list:
            hashed_id = self._cleanAndHashIdentifier(m)
            if hashed_id:
                f.add(hashed_id)
        with open(audience_name + '.buttonaudience', 'wb') as fp:
            f.tofile(fp)
        return 'success'
