from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase
from mock import Mock
from mock import patch

from pybutton.resources import Orders

config = {
    'hostname': 'api.usebutton.com',
    'secure': True,
    'port': 443,
    'timeout': None,
}


class OrdersTestCase(TestCase):

        def test_path(self):
            order = Orders('sk-XXX', config)
            self.assertEqual(order._path(), '/v1/order')
            self.assertEqual(order._path('btnorder-1'), '/v1/order/btnorder-1')

        def test_get(self):
            order = Orders('sk-XXX', config)
            order_response = {'a': 1}

            api_get = Mock()
            api_get.return_value = order_response

            with patch.object(order, 'api_get', api_get):
                response = order.get('btnorder-XXX')

            self.assertEqual(response, order_response)
            api_get.assert_called_with('/v1/order/btnorder-XXX')

        def test_create(self):
            order = Orders('sk-XXX', config)
            order_payload = {'b': 2}
            order_response = {'a': 1}

            api_post = Mock()
            api_post.return_value = order_response

            with patch.object(order, 'api_post', api_post):
                response = order.create(order_payload)

            self.assertEqual(response, order_response)
            api_post.assert_called_with('/v1/order', order_payload)

        def test_update(self):
            order = Orders('sk-XXX', config)
            order_payload = {'b': 2}
            order_response = {'a': 1}

            api_post = Mock()
            api_post.return_value = order_response

            with patch.object(order, 'api_post', api_post):
                response = order.update('btnorder-XXX', order_payload)

            self.assertEqual(response, order_response)
            api_post.assert_called_with(
                '/v1/order/btnorder-XXX',
                order_payload,
            )

        def test_delete(self):
            order = Orders('sk-XXX', config)
            order_response = {'a': 1}

            api_delete = Mock()
            api_delete.return_value = order_response

            with patch.object(order, 'api_delete', api_delete):
                response = order.delete('btnorder-XXX')

            self.assertEqual(response, order_response)
            api_delete.assert_called_with('/v1/order/btnorder-XXX')
