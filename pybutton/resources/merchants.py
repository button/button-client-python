from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pybutton.resources.resource import Resource


class Merchants(Resource):
    '''Manages interacting with Button Merchants via the Button API

    See Resource for class docstring.

    '''

    def all(self, status=None, currency=None):
        '''Get a list of merchants and their configured rates

        Args:
            status (str) optional: A status to filter by.  One of ('approved',
                'pending', or 'available')
            currency (str) optional: An ISO-4217 currency code to filter rates
                by

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        query = {}

        if status:
            query['status'] = status

        if currency:
            query['currency'] = currency

        return self.api_get('/v1/merchants', query=query)
