from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase

from pybutton.response import Response


class ResponseTestCase(TestCase):

    def test_to_dict(self):
        attrs = {'a': 1, 'b': 2}
        response = Response(attrs)

        self.assertEqual(response.to_dict(), attrs)

    def test_access_attribute(self):
        attrs = {'a': 1, 'b': 2}
        response = Response(attrs)

        self.assertEqual(response.a, attrs['a'])
        self.assertEqual(response.b, attrs['b'])
