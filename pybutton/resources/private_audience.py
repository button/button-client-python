from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import hashlib

try:
    import pybloom_live as pl
except:
    pass

from pybutton.resources.resource import Resource


class PrivateAudience(Resource):

    def load(self, filename):
        with open(filename, 'rb') as fp:
            self.private_audience_loaded = pl.BloomFilter.fromfile(fp)
        return 'success'

    def evaluate(self, identifier):
        identifier_clean = identifier.encode('utf-8').lower().strip()
        hashed_identifier = hashlib.sha256(identifier_clean)
        hashed_identifier.update(self.config['private_audience_secret'])
        return hashed_identifier.hexdigest() in self.private_audience_loaded

    def match(self, match_list):
        return_list = []
        for m in match_list:
            m_clean = m.encode('utf-8').lower().strip()
            hashed_identifier = hashlib.sha256(m_clean)
            hashed_identifier.update(self.config['private_audience_secret'])
            if hashed_identifier.hexdigest() in self.private_audience_loaded:
                return_list.append(m)
        return return_list

    def create(self, audience_name, identifier_list, error_rt=0.00001):
        # Initialize Bloom Filter
        f = pl.BloomFilter(capacity=len(identifier_list), error_rate=error_rt)
        for m in identifier_list:
            m_clean = m.encode('utf-8').lower().strip()
            hashed_identifier = hashlib.sha256(m_clean)
            hashed_identifier.update(self.config['private_audience_secret'])
            f.add(hashed_identifier.hexdigest())
        with open(audience_name + '.buttonaudience', 'wb') as fp:
            f.tofile(fp)
        return 'success'
