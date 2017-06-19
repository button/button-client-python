from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pybutton.resources.resource import Resource


class Accounts(Resource):
    '''Manages interacting with Button Accounts via the Button API

    See Resource for class docstring.

    '''

    def all(self):
        '''Get a list of available accounts

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        return self.api_get('/v1/affiliation/accounts')

    def transactions(self, account_id, cursor=None, start=None, end=None):
        '''Get a list of transactions.
        To paginate transactions, pass the result of response.next_cursor() as
        the cursor argument.


        Args:
            account_id (str) optional: A Button account id ('acc-XXX')
            cursor (str) optional: An opaque string that lets you view a
                consistent list of transactions.
            start (ISO-8601 datetime str) optional: Filter out transactions
                created at or after this time.
            end (ISO-8601 datetime str) optional: Filter out transactions
                created before this time.

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        query = {}

        if cursor:
            query['cursor'] = cursor
        if start:
            query['start'] = start
        if end:
            query['end'] = end

        path = '/v1/affiliation/accounts/{0}/transactions'.format(
            account_id
        )

        return self.api_get(path, query=query)
