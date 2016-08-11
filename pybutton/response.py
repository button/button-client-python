from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class Response(object):
    '''The Response class wraps a return value (dict) from an API call.

    It exposes all keys in the underlying response as attributes on the
    instance.

    Args:
        attrs (dict): The underlying response value from an API call

    Attributes:
        * (*): All keys in `attrs` will be exposed as attributes of an instance

    '''

    def __init__(self, attrs):
        self.attrs = attrs

    def to_dict(self):
        '''Return the raw response received from the server'''

        return self.attrs

    def __getattr__(self, attr):
        '''Proxy attribute lookups on an instance down to the response'''

        return self.attrs.get(attr)

    def __repr__(self):
        values = []

        if self.attrs:
            for k, v in self.attrs.items():
                values = values + ['{0}: {1}'.format(k, v)]

        return '<class pybutton.Response {0}>'.format(', '.join(values))
