from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase
from mock import Mock
from mock import patch

from pybutton.resources import Links

config = {
    'hostname': 'api.usebutton.com',
    'secure': True,
    'port': 443,
    'timeout': None,
}


class LinksTestCase(TestCase):

        def test_create(self):
            link = Links('https://test.com', config)
            link_payload = {'b': 2}
            link_response = {'a': 1}

            api_post = Mock()
            api_post.return_value = link_response

            with patch.object(link, 'api_post', api_post):
                response = link.create(link_payload)

            self.assertEqual(response, link_response)
            api_post.assert_called_with('/v1/links', link_payload)

        def test_get_info(self):
            link = Links('https://test.com', config)
            link_payload = {'b': 2}
            link_response = {'a': 1}

            api_post = Mock()
            api_post.return_value = link_response

            with patch.object(link, 'api_post', api_post):
                response = link.create(link_payload)

            self.assertEqual(response, link_response)
            api_post.assert_called_with('/v1/links/info', link_payload)
