from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from unittest import TestCase
from mock import Mock
from mock import patch

from pybutton.request import HTTPError
from pybutton.resources.resource import Resource
from pybutton.error import HTTPResponseError

config = {
    'hostname': 'api.usebutton.com',
    'secure': True,
    'port': 443,
    'timeout': None,
    'api_version': None,
}


class ResourceTestCase(TestCase):

    @patch('pybutton.resources.resource.request')
    def test_api_request(self, request):
        resource_response = {'a': 1}
        request.return_value = {'object': resource_response}
        resource = Resource('sk-XXX', config)
        response = resource._api_request('/v1/api', 'GET')

        args = request.call_args[0]
        self.assertEqual(response.data(), resource_response)
        self.assertEqual(args[0], 'https://api.usebutton.com:443/v1/api')
        self.assertEqual(args[1], 'GET')
        self.assertTrue(len(args[2]['User-Agent']) != 0)
        self.assertEqual(args[2]['Authorization'], 'Basic c2stWFhYOg==')
        self.assertTrue('X-Button-API-Version' not in args[2])
        self.assertEqual(args[3], None)

    @patch('pybutton.resources.resource.request')
    def test_api_request_with_other_methods(self, request):
        resource_response = {'a': 1}
        request.return_value = {'object': resource_response}
        resource = Resource('sk-XXX', config)
        response = resource._api_request('/v1/api', 'POST')

        args = request.call_args[0]
        self.assertEqual(response.data(), resource_response)
        self.assertEqual(args[0], 'https://api.usebutton.com:443/v1/api')
        self.assertEqual(args[1], 'POST')
        self.assertTrue(len(args[2]['User-Agent']) != 0)
        self.assertEqual(args[2]['Authorization'], 'Basic c2stWFhYOg==')
        self.assertEqual(args[3], None)

    @patch('pybutton.resources.resource.request')
    def test_api_request_with_other_paths(self, request):
        resource_response = {'a': 1}
        request.return_value = {'object': resource_response}
        resource = Resource('sk-XXX', config)
        response = resource._api_request('/v2/api', 'GET')

        args = request.call_args[0]
        self.assertEqual(response.data(), resource_response)
        self.assertEqual(args[0], 'https://api.usebutton.com:443/v2/api')
        self.assertEqual(args[1], 'GET')
        self.assertTrue(len(args[2]['User-Agent']) != 0)
        self.assertEqual(args[2]['Authorization'], 'Basic c2stWFhYOg==')
        self.assertEqual(args[3], None)

    @patch('pybutton.resources.resource.request')
    def test_api_request_with_data(self, request):
        data = {'c': 3}
        resource_response = {'a': 1}
        request.return_value = {'object': resource_response}
        resource = Resource('sk-XXX', config)
        response = resource._api_request('/v2/api', 'GET', data)

        args = request.call_args[0]
        self.assertEqual(response.data(), resource_response)
        self.assertEqual(args[0], 'https://api.usebutton.com:443/v2/api')
        self.assertEqual(args[1], 'GET')
        self.assertTrue(len(args[2]['User-Agent']) != 0)
        self.assertEqual(args[2]['Authorization'], 'Basic c2stWFhYOg==')
        self.assertEqual(args[3], data)

    @patch('pybutton.resources.resource.request')
    def test_api_request_with_api_version(self, request):
        config = {
            'hostname': 'api.usebutton.com',
            'secure': True,
            'port': 443,
            'timeout': None,
            'api_version': '2017-01-01',
        }

        request.return_value = {'object': {}}
        resource = Resource('sk-XXX', config)
        resource._api_request('/v2/api', 'GET')

        args = request.call_args[0]
        self.assertEqual(args[2]['X-Button-API-Version'], '2017-01-01')

    @patch('pybutton.resources.resource.request')
    def test_api_request_with_error(self, request):
        data = {'c': 3}

        fp = Mock()
        fp.read.return_value = '{}'

        def side_effect(*args):
            raise HTTPError('url', 404, 'bloop', {}, fp)

        request.side_effect = side_effect
        resource = Resource('sk-XXX', config)

        try:
            resource._api_request('/v2/api', 'GET', data)
            self.assertTrue(False)
        except HTTPResponseError as e:
            self.assertEqual(str(e), '404 bloop')
            self.assertEqual(e.status_code, 404)
            self.assertTrue(e.cause is not None)

    @patch('pybutton.resources.resource.request')
    def test_api_request_with_byte_response(self, request):
        data = {'c': 3}

        fp = Mock()
        fp.read.return_value = """
            { "error": { "message": "bloop failed" } }
        """.encode()

        def side_effect(*args):
            raise HTTPError('url', 404, 'bloop', {}, fp)

        request.side_effect = side_effect
        resource = Resource('sk-XXX', config)

        try:
            resource._api_request('/v2/api', 'GET', data)
            self.assertTrue(False)
        except HTTPResponseError as e:
            self.assertEqual(str(e), 'bloop failed')
            self.assertEqual(e.status_code, 404)
            self.assertTrue(e.cause is not None)

    @patch('pybutton.resources.resource.request')
    def test_api_get(self, request):
        resource_response = {'a': 1}
        request.return_value = {'object': resource_response}
        resource = Resource('sk-XXX', config)
        response = resource.api_get('/v1/api')

        args = request.call_args[0]
        self.assertEqual(response.data(), resource_response)
        self.assertEqual(args[0], 'https://api.usebutton.com:443/v1/api')
        self.assertEqual(args[1], 'GET')
        self.assertTrue(len(args[2]['User-Agent']) != 0)
        self.assertEqual(args[2]['Authorization'], 'Basic c2stWFhYOg==')
        self.assertEqual(args[3], None)

    @patch('pybutton.resources.resource.request')
    def test_api_post(self, request):
        request_payload = {'c': 3}
        resource_response = {'a': 1}
        request.return_value = {'object': resource_response}
        resource = Resource('sk-XXX', config)
        response = resource.api_post('/v1/api', request_payload)

        args = request.call_args[0]
        self.assertEqual(response.data(), resource_response)
        self.assertEqual(args[0], 'https://api.usebutton.com:443/v1/api')
        self.assertEqual(args[1], 'POST')
        self.assertTrue(len(args[2]['User-Agent']) != 0)
        self.assertEqual(args[2]['Authorization'], 'Basic c2stWFhYOg==')
        self.assertEqual(args[3], request_payload)

    @patch('pybutton.resources.resource.request')
    def test_api_delete(self, request):
        resource_response = {'a': 1}
        request.return_value = {'object': resource_response}
        resource = Resource('sk-XXX', config)
        response = resource.api_delete('/v1/api')

        args = request.call_args[0]
        self.assertEqual(response.data(), resource_response)
        self.assertEqual(args[0], 'https://api.usebutton.com:443/v1/api')
        self.assertEqual(args[1], 'DELETE')
        self.assertTrue(len(args[2]['User-Agent']) != 0)
        self.assertEqual(args[2]['Authorization'], 'Basic c2stWFhYOg==')
        self.assertEqual(args[3], None)
