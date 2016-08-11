from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
import json

from .error import ButtonClientError

# `pybutton.request` will expose 4 attributes, all specific to the major
# version of the interpreter:
#
# * `Request`:  The request class used to make network calls
# * `urlopen`:  The function used to make the network call
# * `HTTPError`:  The Exception class raised by `urlopen`
# * `request`:  A function for making a network request
#
if sys.version_info[0] == 3:
    from urllib.request import Request
    from urllib.request import urlopen
    from urllib.error import HTTPError

    def request(url, method, headers, data=None):
        ''' Make an HTTP request in Python 3.x

        This method will abstract the underlying organization and invocation of
        the Python 3 HTTP standard lib implementation.

        Args:
            url (str): The url of the resource to request
            method (str): The HTTP method
            headers (dict): HTTP Headers as key value pairs to include
            data (dict) optional: Data to be encoded as JSON and included in
                the request body

        Raises:
            urllib.error.HTTPError
            pybutton.ButtonClientError

        Returns:
            (dict): The response from the server interpreted as JSON.

        '''

        encoded_data = json.dumps(data).encode('utf8') if data else None
        request = Request(url, data=encoded_data, headers=headers)
        request.get_method = lambda: method

        if data:
            request.add_header('Content-Type', 'application/json')

        response = urlopen(request).read().decode('utf8')

        try:
            return json.loads(response)
        except ValueError:
            raise ButtonClientError('Invalid response: {0}'.format(response))

    __all__ = [Request, urlopen, HTTPError, request]

else:
    from urllib2 import Request
    from urllib2 import urlopen
    from urllib2 import HTTPError

    def request(url, method, headers, data=None):
        ''' Make an HTTP request in Python 2.x

        This method will abstract the underlying organization and invocation of
        the Python 2 HTTP standard lib implementation.

        Args:
            url (str): The url of the resource to request
            method (str): The HTTP method
            headers (dict): HTTP Headers as key value pairs to include
            data (dict) optional: Data to be encoded as JSON and included in
                the request body

        Raises:
            urllib2.HTTPError
            pybutton.ButtonClientError

        Returns:
            (dict): The response from the server interpreted as JSON.

        '''

        request = Request(url)
        request.get_method = lambda: method

        for k, v in headers.iteritems():
            request.add_header(k, v)

        if data:
            request.add_header('Content-Type', 'application/json')
            request.add_data(json.dumps(data))

        response = urlopen(request).read()

        try:
            return json.loads(response)
        except ValueError:
            raise ButtonClientError('Invalid response: {0}'.format(response))

    __all__ = [Request, urlopen, HTTPError, request]
