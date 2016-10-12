from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase

from pybutton.response import Response


class ResponseTestCase(TestCase):

    def test_data(self):
        response_data = {'a': 1, 'b': 2}
        response = Response({}, response_data)
        self.assertEqual(response.data(), response_data)

        response_data = [{'a': 1, 'b': 2}, {'c': 3}, {'d': 4}]
        response = Response({}, response_data)
        self.assertEqual(response.data(), response_data)

    def test_cursors(self):
        response_data = {'a': 1, 'b': 2}

        meta = {
            'status': 'ok',
            'next': """https://api.usebutton.com:443/v1/affiliation/accounts/
                acc-123/transactions?cursor=abc""",
            'prev': """https://api.usebutton.com:443/v1/affiliation/accounts/
                acc-123/transactions?cursor=def""",
        }
        response = Response(meta, response_data)

        self.assertEqual(response.nextCursor(), 'abc')
        self.assertEqual(response.prevCursor(), 'def')

        meta = {
            'status': 'ok',
            'next': None,
            'prev': 'https://',
        }
        response = Response(meta, response_data)

        self.assertEqual(response.nextCursor(), None)
        self.assertEqual(response.prevCursor(), None)

        meta = {
            'status': 'ok',
            'next': '12345',
            'prev': """https://api.usebutton.com:443/v1/affiliation/accounts/
                acc-123/transactions?c=abc"""
        }
        response = Response(meta, response_data)

        self.assertEqual(response.nextCursor(), None)
        self.assertEqual(response.prevCursor(), None)


    def test_repr(self):
        response_data = {'a': 1}
        response = Response({}, response_data)
        self.assertEqual(response.__repr__(), '<class pybutton.Response a: 1>')

        response_data = [{'a': 1, 'b': 2}, {'c': 3}, {'d': 4}]
        response = Response({}, response_data)
        self.assertEqual(
            response.__repr__(),
            '<class pybutton.Response [3 elements]>'
        )

        response = Response({}, None)
        self.assertEqual(response.__repr__(), '<class pybutton.Response>')
