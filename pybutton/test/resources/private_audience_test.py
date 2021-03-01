from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase

from pybutton.resources import PrivateAudience

config = {}


class PrivateAudienceTestCase(TestCase):

        def test_create_audience(self):
            private_audience = PrivateAudience('sk-XXX', config)
            response = private_audience.create(
                'test_audience',
                ['bloop', 'blip']
            )
            self.assertEqual(response, 'success')

        def test_load_and_evaluate_audience(self):
            private_audience = PrivateAudience('sk-XXX', config)
            response = private_audience.load('test_audience.buttonaudience')
            self.assertEqual(response, 'success')
            self.assertEqual(private_audience.evaluate('bloop'), True)
            self.assertEqual(private_audience.evaluate('blop'), False)
            self.assertEqual(private_audience.match(
                ['bloop', 'blip', 'bloom']), ['bloop', 'blip'])

        def test_load_and_evaluate_audience_wrong_key(self):
            private_audience = PrivateAudience('sk-YYY', config)
            response = private_audience.load('test_audience.buttonaudience')
            self.assertEqual(response, 'success')
            self.assertEqual(private_audience.evaluate('bloop'), False)
            self.assertEqual(private_audience.evaluate('blop'), False)
            self.assertNotEqual(private_audience.match(
                ['bloop', 'blip', 'bloom']), ['bloop', 'blip'])
