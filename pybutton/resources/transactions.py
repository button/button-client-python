from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pybutton.resources.resource import Resource


class Transactions(Resource):
    """Manages interacting with Button Transactions via the Button API

    See Resource for class docstring.

    """

    def all(self, cursor=None, start=None, end=None, time_field=None):
        """Get a list of transactions.
        To paginate transactions, pass the result of response.next_cursor() as
        the cursor argument.
        Unlike Accounts.transactions, which retrieves transactions only for a
        single account, Transactions.all retrieves all of an organization's
        transactions.


        Args:
            cursor (str) optional: An opaque string that lets you view a
                consistent list of transactions.
            start (ISO-8601 datetime str) optional: Filter out transactions
                created at or after this time.
            end (ISO-8601 datetime str) optional: Filter out transactions
                created before this time.
            time_field (str) optional: Which time field ``start`` and ``end``
                filter on. Defaults to created_date.

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        """

        query = {}

        if cursor:
            query['cursor'] = cursor
        if start:
            query['start'] = start
        if end:
            query['end'] = end
        if time_field:
            query['time_field'] = time_field

        return self.api_get('/v1/affiliation/transactions', query=query)
