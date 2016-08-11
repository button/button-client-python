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
