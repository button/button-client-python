from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase
from mock import Mock
from mock import patch

from pybutton import constants
from pybutton.resources import Transactions

config = {
    'hostname': 'api.usebutton.com',
    'secure': True,
    'port': 443,
    'timeout': None,
}


class TransactionsTestCase(TestCase):

        def test_all(self):
            transactions = Transactions('sk-XXX', config)
            transaction_response = [{'a': 1}, {'b': 2}]

            api_get = Mock()
            api_get.return_value = transaction_response

            with patch.object(transactions, 'api_get', api_get):
                response = transactions.all(
                    cursor='abc',
                    start='2016-09-15T00:00:00.000Z',
                    end='2016-09-30T00:00:00.000Z'
                )
                self.assertEqual(
                    api_get.call_args[0][0],
                    '/v1/affiliation/transactions'
                )
                self.assertEqual(response, transaction_response)
                query = api_get.call_args[1]['query']
                self.assertEqual(query['cursor'], 'abc')
                self.assertEqual(query['start'], '2016-09-15T00:00:00.000Z')
                self.assertEqual(query['end'], '2016-09-30T00:00:00.000Z')

                response = transactions.all(
                    cursor='abc',
                    start='2016-09-15T00:00:00.000Z',
                    end='2016-09-30T00:00:00.000Z',
                    time_field=constants.TIME_FIELD_MODIFIED
                )
                self.assertEqual(response, transaction_response)
                query = api_get.call_args[1]['query']
                self.assertEqual(query['time_field'], 'modified_date')
