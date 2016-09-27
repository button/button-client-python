from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase

from pybutton.client import Client
from pybutton import ButtonClientError


class ClientTestCase(TestCase):

    def test_requires_api_key(self):
        try:
            Client()
            self.assertTrue(False)
        except TypeError:
            pass

        try:
            Client('')
            self.assertTrue(False)
        except ButtonClientError:
            pass

        try:
            Client(None)
            self.assertTrue(False)
        except ButtonClientError:
            pass

    def test_orders(self):
        client = Client('sk-XXX')
        self.assertTrue(client.orders is not None)

    def test_config(self):
        client = Client('sk-XXX')

        # Defaults
        config = client._config_with_defaults({})

        self.assertEqual(config, {
            'hostname': 'api.usebutton.com',
            'port': 443,
            'secure': True,
            'timeout': None
        })

        # Port and timeout overrides
        config = client._config_with_defaults({
            'port': 88,
            'timeout': 5
        })

        self.assertEqual(config, {
            'hostname': 'api.usebutton.com',
            'port': 88,
            'secure': True,
            'timeout': 5
        })

        # Hostname and secure overrides
        config = client._config_with_defaults({
            'hostname': 'localhost',
            'secure': False
        })

        self.assertEqual(config, {
            'hostname': 'localhost',
            'port': 80,
            'secure': False,
            'timeout': None
        })
