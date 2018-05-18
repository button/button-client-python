from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from base64 import b64encode
from platform import python_version
import json

from pybutton.response import Response
from pybutton.error import HTTPResponseError
from pybutton.version import VERSION
from pybutton.request import request
from pybutton.request import request_url
from pybutton.request import HTTPError

USER_AGENT = 'pybutton/{0} python/{1}'.format(VERSION, python_version())


class Resource(object):
    '''Abstract Base Class for managing a remote resource in our API.

    Includes handy methods for making HTTP calls against our API and returning
    payloads in a standardized format (namely, pybutton.Response objects).

    Args:
        api_key (string): Your organization's API key.  Do find yours at
            https://app.usebutton.com/settings/organization.

        config (dict): Configuration options for the client. Options include:
            hostname: Defaults to api.usebutton.com.
            port: Defaults to 443 if config.secure, else defaults to 80.
            secure: Whether or not to use HTTPS. Defaults to True.
            timeout: The time in seconds for network requests to abort.
              Defaults to None.
              (N.B: Button's API is only exposed through HTTPS. This option is
              provided purely as a convenience for testing and development.)

    Raises:
        pybutton.ButtonClientError
        pybutton.HTTPResponseError

    '''

    def __init__(self, api_key, config):
        self.api_key = api_key
        self.config = config

    def api_get(self, path, query=None):
        '''Make an HTTP GET request

        Args:
            path (str): The path of the resource

        Returns:
            (pybutton.Response): The API response

        '''
        return self._api_request(path, 'GET', query=query)

    def api_post(self, path, data):
        '''Make an HTTP POST request

        Args:
            path (str): The path of the resource
            data (dict): The data to POST

        Returns:
            (pybutton.Response): The API response

        '''
        return self._api_request(path, 'POST', data)

    def api_delete(self, path):
        '''Make an HTTP DELETE request

        Args:
            path (str): The path of the resource

        Returns:
            (pybutton.Response): The API response

        '''
        return self._api_request(path, 'DELETE')

    def _headers(self):
        '''Generate the HTTP headers used for a request
        '''

        api_key_bytes = '{0}:'.format(self.api_key).encode()
        authorization = b64encode(api_key_bytes).decode()

        headers = {
            'Authorization': 'Basic {0}'.format(authorization),
            'User-Agent': USER_AGENT,
        }

        if self.config['api_version']:
            headers['X-Button-API-Version'] = self.config['api_version']

        return headers

    def _api_request(self, path, method, data=None, query=None):
        '''Make an HTTP request

        Any data provided will be JSON encoded an included as part of the
        request body.  Additionally, an Authorization header will be set based
        on the instance's API key and a User-Agent header will be set with the
        interpreter version and pybutton client version.

        Args:
            path (str): The path of the resource
            method (str): The HTTP method
            data (dict): The data to POST

        Returns:
            (pybutton.Response): The API response

        '''

        url = request_url(
            self.config['secure'],
            self.config['hostname'],
            self.config['port'],
            path,
            query,
        )

        try:
            resp = request(
                url,
                method,
                self._headers(),
                data,
                self.config['timeout'],
            )

            return Response(
                resp.get('meta', {}),
                # Response info may have 'object' or 'objects' key, depending
                # on whether there are 1 or multiple results.
                resp.get('object', resp.get('objects'))
            )
        except HTTPError as e:
            response = e.read()
            fallback = '{0} {1}'.format(e.code, e.msg)

            if isinstance(response, bytes):
                data = response.decode('utf8')
            else:
                data = response

            error = json.loads(data).get('error', {})
            message = error.get('message', fallback)
            raise HTTPResponseError(message, status_code=e.code, cause=e)
