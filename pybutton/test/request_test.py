from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
from unittest import TestCase
from mock import Mock
from mock import patch

from pybutton.request import request
from pybutton.request import request_url
from pybutton.request import query_dict
from pybutton import ButtonClientError


class RequestTestCasePy2(TestCase):

    @patch('pybutton.request.urlopen')
    @patch('pybutton.request.Request')
    def test_get_request(self, MockRequest, mock_url_open):
        if sys.version_info[0] == 2:
            url = 'http://usebutton.com/api'
            method = 'GET'
            headers = {'a': 1, 'b': 2}

            instance = MockRequest.return_value

            mock_response = Mock()
            mock_response.read.return_value = '{ "a": 1 }'
            mock_url_open.return_value = mock_response

            response = request(url, method, headers)

            MockRequest.assert_called_with(url)
            self.assertEqual(instance.get_method(), method)
            instance.add_header.assert_called_with('b', 2)
            self.assertEqual(response, {'a': 1})

    @patch('pybutton.request.urlopen')
    @patch('pybutton.request.Request')
    def test_post_request(self, MockRequest, mock_url_open):
        if sys.version_info[0] == 2:
            url = 'http://usebutton.com/api'
            method = 'POST'
            headers = {}

            instance = MockRequest.return_value

            mock_response = Mock()
            mock_response.read.return_value = '{ "a": 1 }'
            mock_url_open.return_value = mock_response

            response = request(url, method, headers)

            MockRequest.assert_called_with(url)
            self.assertEqual(instance.get_method(), method)
            self.assertEqual(response, {'a': 1})

    @patch('pybutton.request.urlopen')
    @patch('pybutton.request.Request')
    def test_post_request_with_data(self, MockRequest, mock_url_open):
        if sys.version_info[0] == 2:
            url = 'http://usebutton.com/api'
            method = 'POST'
            headers = {}
            data = {'a': {'b': 'c'}}

            instance = MockRequest.return_value

            mock_response = Mock()
            mock_response.read.return_value = '{ "a": 1 }'
            mock_url_open.return_value = mock_response

            response = request(url, method, headers, data=data)

            MockRequest.assert_called_with(url)
            self.assertEqual(instance.get_method(), method)

            instance.add_data.assert_called_with('{"a": {"b": "c"}}')

            instance.add_header.assert_called_with(
                'Content-Type',
                'application/json'
            )

            self.assertEqual(response, {'a': 1})

    @patch('pybutton.request.urlopen')
    @patch('pybutton.request.Request')
    def test_raises_with_invalid_response_data(self, MockRequest,
                                               mock_url_open):
        if sys.version_info[0] == 2:
            url = 'http://usebutton.com/api'
            method = 'GET'
            headers = {}

            mock_response = Mock()
            mock_response.read.return_value = 'wat'
            mock_url_open.return_value = mock_response

            try:
                request(url, method, headers)
                self.assertTrue(False)
            except ButtonClientError as e:
                # We expect the generic ButtonClientError, and not a subclass,
                # in this condition.
                assert type(e) is ButtonClientError


class RequestTestCasePy3(TestCase):

    @patch('pybutton.request.urlopen')
    @patch('pybutton.request.Request')
    def test_get_request(self, MockRequest, mock_url_open):
        if sys.version_info[0] == 3:
            url = 'http://usebutton.com/api'
            method = 'GET'
            headers = {'a': 1, 'b': 2}

            instance = MockRequest.return_value

            mock_response = Mock()
            mock_response.read.return_value = '{ "a": 1 }'.encode()
            mock_url_open.return_value = mock_response

            response = request(url, method, headers)

            MockRequest.assert_called_with(url, data=None, headers=headers)
            self.assertEqual(instance.get_method(), method)
            self.assertEqual(response, {'a': 1})

    @patch('pybutton.request.urlopen')
    @patch('pybutton.request.Request')
    def test_post_request(self, MockRequest, mock_url_open):
        if sys.version_info[0] == 3:
            url = 'http://usebutton.com/api'
            method = 'POST'
            headers = {}

            instance = MockRequest.return_value

            mock_response = Mock()
            mock_response.read.return_value = '{ "a": 1 }'.encode()
            mock_url_open.return_value = mock_response

            response = request(url, method, headers)

            MockRequest.assert_called_with(url, data=None, headers=headers)
            self.assertEqual(instance.get_method(), method)
            self.assertEqual(response, {'a': 1})

    @patch('pybutton.request.urlopen')
    @patch('pybutton.request.Request')
    def test_post_request_with_data(self, MockRequest, mock_url_open):
        if sys.version_info[0] == 3:
            url = 'http://usebutton.com/api'
            method = 'POST'
            headers = {}
            data = {'a': {'b': 'c'}}

            instance = MockRequest.return_value

            mock_response = Mock()
            mock_response.read.return_value = '{ "a": 1 }'.encode()
            mock_url_open.return_value = mock_response

            response = request(url, method, headers, data=data)

            MockRequest.assert_called_with(
                url,
                data=json.dumps(data).encode(),
                headers=headers
            )

            self.assertEqual(instance.get_method(), method)

            instance.add_header.assert_called_with(
                'Content-Type',
                'application/json'
            )

            self.assertEqual(response, {'a': 1})

    @patch('pybutton.request.urlopen')
    @patch('pybutton.request.Request')
    def test_raises_with_invalid_response_data(self, MockRequest,
                                               mock_url_open):
        if sys.version_info[0] == 3:
            url = 'http://usebutton.com/api'
            method = 'GET'
            headers = {}

            mock_response = Mock()
            mock_response.read.return_value = 'wat'.encode()
            mock_url_open.return_value = mock_response

            try:
                request(url, method, headers)
                self.assertTrue(False)
            except ButtonClientError:
                pass

    def test_request_url(self):
        path = request_url(
            True,
            'api.usebutton.com',
            443,
            '/v1/api/btnorder-XXX'
        )

        self.assertEqual(
            path,
            'https://api.usebutton.com:443/v1/api/btnorder-XXX'
        )

        path = request_url(False, 'localhost', 80, '/v1/api/btnorder-XXX')
        self.assertEqual(path, 'http://localhost:80/v1/api/btnorder-XXX')

    def test_query_dict(self):
        url = 'https://api.usebutton.com:/test/url?cursor=test_cursor'
        result = query_dict(url)
        self.assertEqual(result.get('cursor'), ['test_cursor'])
        self.assertEqual(result.get('random_key'), None)

        no_query_url = 'https://api.usebutton.com:/test/url'
        result = query_dict(no_query_url)
        self.assertEqual(result.get('cursor'), None)
