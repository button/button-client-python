from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase
from mock import Mock
from mock import patch

from pybutton.resources import Merchants

config = {
    'hostname': 'api.usebutton.com',
    'secure': True,
    'port': 443,
    'timeout': None,
}


class MerchantsTestCase(TestCase):

        def test_all(self):
            merchants = Merchants('sk-XXX', config)
            merchants_response = [{'a': 1}, {'b': 2}]

            api_get = Mock()
            api_get.return_value = merchants_response

            with patch.object(merchants, 'api_get', api_get):
                response = merchants.all()

            self.assertEqual(response, merchants_response)
            api_get.assert_called_with('/v1/merchants', query={})

        def test_all_with_query(self):
            merchants = Merchants('sk-XXX', config)
            merchants_response = [{'a': 1}, {'b': 2}]

            api_get = Mock()
            api_get.return_value = merchants_response

            with patch.object(merchants, 'api_get', api_get):
                response = merchants.all(status='pending', currency='GBP')

            self.assertEqual(response, merchants_response)
            api_get.assert_called_with(
                '/v1/merchants',
                query={'status': 'pending', 'currency': 'GBP'}
            )
