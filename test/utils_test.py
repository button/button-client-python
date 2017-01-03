from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase

from pybutton.utils import is_webhook_authentic


class UtilsTestCase(TestCase):

    def test_is_webhook_authentic(self):
        signature = (
            '79a3a5291c94340ff0058a631906375'
            '768d706357ee86826c3c692e6b9aa6817'
        )
        payload = '{ "a": 1 }'

        self.assertFalse(is_webhook_authentic('secret', payload, 'XXX'))
        self.assertTrue(is_webhook_authentic('secret', payload, signature))
        self.assertFalse(is_webhook_authentic('secret?', payload, signature))
        self.assertFalse(is_webhook_authentic(
            'secret', '{ "a": 2 }', signature)
        )

    def test_is_webhook_authentic_unicode_payload(self):
        signature = (
            '3040cf48ab225ca539c1d23841175bc2'
            '2e565cdb0975bd690ecaeca2c39dfcf7'
        )

        self.assertTrue(
            is_webhook_authentic('secret', '{ "a": \u1f60e }', signature)
        )

    def test_is_webhook_authentic_byte_strings(self):
        signature = (
            '79a3a5291c94340ff0058a6319063757'
            '68d706357ee86826c3c692e6b9aa6817'
        )
        payload = b'{ "a": 1 }'

        self.assertFalse(is_webhook_authentic(b'secret', payload, 'XXX'))
        self.assertTrue(is_webhook_authentic(b'secret', payload, signature))
        self.assertFalse(is_webhook_authentic(b'secret?', payload, signature))
        self.assertFalse(
            is_webhook_authentic(b'secret', b'{ "a": 2 }', signature)
        )
