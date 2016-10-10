from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase
from mock import Mock
from mock import patch

from pybutton.resources import Accounts

config = {
    'hostname': 'api.usebutton.com',
    'secure': True,
    'port': 443,
    'timeout': None
}


class AccountsTestCase(TestCase):

        def test_path(self):
            account = Accounts('sk-XXX', config)
            self.assertEqual(account._path(), '/v1/affiliation/accounts')
            self.assertEqual(
                account._path('acc-123'),
                '/v1/affiliation/accounts/acc-123/transactions'
            )

        def test_all(self):
            account = Accounts('sk-XXX', config)
            account_response = [{'a': 1}, {'b': 2}]

            api_get = Mock()
            api_get.return_value = account_response

            with patch.object(account, 'api_get', api_get):
                response = account.all()

            self.assertEqual(response, account_response)
            api_get.assert_called_with('/v1/affiliation/accounts')

        def test_transactions(self):
            account = Accounts('sk-XXX', config)
            account_response = [{'a': 1}, {'b': 2}]

            api_get = Mock()
            api_get.return_value = account_response

            with patch.object(account, 'api_get', api_get):
                response = account.transactions('acc-123')
                self.assertEqual(response, account_response)
                self.assertEqual(
                    api_get.call_args[0][0],
                    '/v1/affiliation/accounts/acc-123/transactions'
                )

                response = account.transactions(
                    'acc-123',
                    cursor='abc',
                    start='2016-09-15T00:00:00.000Z',
                    end='2016-09-30T00:00:00.000Z'
                )
                self.assertEqual(response, account_response)
                query = api_get.call_args[1]['query']
                self.assertEqual(query['cursor'], 'abc')
                self.assertEqual(query['start'], '2016-09-15T00:00:00.000Z')
                self.assertEqual(query['end'], '2016-09-30T00:00:00.000Z')
