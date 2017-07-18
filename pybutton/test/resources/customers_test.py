from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase
from mock import Mock
from mock import patch

from pybutton.resources import Customers

config = {
    'hostname': 'api.usebutton.com',
    'secure': True,
    'port': 443,
    'timeout': None,
}


class CustomersTestCase(TestCase):

    def test_path(self):
        customer = Customers('sk-XXX', config)
        self.assertEqual(customer._path(), '/v1/customers')
        self.assertEqual(
            customer._path('customer-1'),
            '/v1/customers/customer-1'
        )

    def test_get(self):
        customer = Customers('sk-XXX', config)
        customer_response = {'a': 1}

        api_get = Mock()
        api_get.return_value = customer_response

        with patch.object(customer, 'api_get', api_get):
            response = customer.get('customer-XXX')

        self.assertEqual(response, customer_response)
        api_get.assert_called_with('/v1/customers/customer-XXX')

    def test_create(self):
        customer = Customers('sk-XXX', config)
        customer_payload = {'b': 2}
        customer_response = {'a': 1}

        api_post = Mock()
        api_post.return_value = customer_response

        with patch.object(customer, 'api_post', api_post):
            response = customer.create(customer_payload)

        self.assertEqual(response, customer_response)
        api_post.assert_called_with('/v1/customers', customer_payload)
