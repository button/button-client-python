from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class ButtonClientError(Exception):
    '''An Exception class for all pybutton understood errors.
    '''


class HTTPResponseError(ButtonClientError):
    '''A non-success HTTP response was returned from the remote API.

    The HTTP response status code can be retrieved from the
    `.status_code` property.

    The original error object can be retrieved from the
    `.cause` property.
    '''
    def __init__(self, message, status_code, cause):
        super(HTTPResponseError, self).__init__(message)
        self.status_code = status_code
        self.cause = cause
