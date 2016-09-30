from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .resource import Resource


class Accounts(Resource):
    '''Manages interacting with Button Orders with the Button API

    Args:
        api_key (string): Your organization's API key.  Do find yours at
                https://app.usebutton.com/settings/organization.
        config (dict): Configuration options for the client. Options include:
            hostname: Defaults to api.usebutton.com.
            port: Defaults to 443 if config.secure, else defaults to 80.
            secure: Whether or not to use HTTPS. Defaults to True.
            timeout: The time in seconds for network requests to abort. Defaults to None.
              (N.B: Button's API is only exposed through HTTPS. This option is provided purely as a convenience for testing and development.)

    Raises:
        pybutton.ButtonClientError

    '''

    def _path(self, account_id=None):
        '''Format a url path

        Args:
            account_id (str) optional: A Button account id ('acc-XXX')
            query (dict) optional: A dictionary of key: value query parameters

        Returns:
            (str): The formatted path

        '''

        if account_id:
            return '/v1/affiliation/accounts/{0}/transactions'.format(account_id)
        else:
            return '/v1/affiliation/accounts'

    def all(self):
        '''Get a list of available accounts

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        return self.api_get(self._path())

    def transactions(self, account_id, cursor=None, start=None, end=None):
        '''Get a list of transactions.
        To paginate transactions, use the meta.next URL as your next request URL until it is null.

        Args:
            account_id (str) optional: A Button account id ('acc-XXX')
            cursor (str) optional: An opaque string that lets you view a consistent list of transactions.
            start (ISO-8601 datetime str) optional: Filter transactions created at or after this time.
            end (ISO-8601 datetime str) optional: Filter transactions created before this time.

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

        return self.api_get(self._path(account_id), query=query)
