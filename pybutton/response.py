from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .request import urlparse
from .request import parse_qs

class Response(object):
    '''The Response class wraps the returned values from an API call.

    It exposes the response data via the `data` method and cursors for pagination via the `next`/`prev` methods.

    Args:
        meta (dict): The metadata from an API call
        data (dict or array<dict>): The response elements from an API call

    Attributes:
        * (*): All keys in `attrs` will be exposed as attributes of an instance

    '''

    def __init__(self, meta, response_data):
        self.meta = meta
        self.response_data = response_data

    def data(self):
        '''Return the raw response element(s) received from the server. May be a single dict or an array of dicts.'''
        return self.response_data

    def next(self):
        '''For paginated responses, return the url used to fetch the next elements'''
        return self._format_cursor(self.meta.get('next'))

    def prev(self):
        '''For paginated responses, return the url used to fetch the previous elements'''
        return self._format_cursor(self.meta.get('prev'))

    def __repr__(self):
        values = []

        if isinstance(self.response_data, dict):
            for k, v in self.response_data.items():
                values = values + ['{0}: {1}'.format(k, v)]
            return '<class pybutton.Response {0}>'.format(', '.join(values))
        elif isinstance(self.response_data, list):
            return '<class pybutton.Response [{0} elements]>'.format(len(self.response_data))
        else:
            return '<class pybutton.Response>'

    def _format_cursor(self, cursor_url):
        if cursor_url:
            query_string = urlparse(cursor_url)[4]
            query = parse_qs(query_string)

            return query['cursor'][0]
