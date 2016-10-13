from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .request import query_dict


class Response(object):
    '''The Response class wraps the returned values from an API call.

    It exposes the response data via the `data` method and cursors for
    pagination via the `next_cursor`/`prev_cursor` methods.

    Args:
        meta (dict): The metadata from an API call
        response_data (dict or array<dict>): The response elements from an
            API call

    Attributes:
        * (*): All keys in `attrs` will be exposed as attributes of an instance

    '''

    classPrefix = 'class pybutton.Response'

    def __init__(self, meta, response_data):
        self.meta = meta
        self.response_data = response_data

    def data(self):
        '''Return the raw response element(s) received from the server.
           May be a single dict or an array of dicts.
        '''
        return self.response_data

    def next_cursor(self):
        '''For paginated responses, returns the url used to fetch
            the next elements.
        '''
        return self._format_cursor(self.meta.get('next'))

    def prev_cursor(self):
        '''For paginated responses, returns the url used to fetch
            the previous elements.
        '''
        return self._format_cursor(self.meta.get('prev'))

    def __repr__(self):
        if isinstance(self.response_data, dict):
            values = []
            for k, v in self.response_data.items():
                values = values + ['{0}: {1}'.format(k, v)]
            return '<{0} {1}>'.format(
                Response.classPrefix,
                ', '.join(values)
            )
        elif isinstance(self.response_data, list):
            return '<{0} [{1} elements]>'.format(
                Response.classPrefix,
                len(self.response_data)
            )
        else:
            return '<class pybutton.Response>'

    def _format_cursor(self, cursor_url):
        if cursor_url:
            query = query_dict(cursor_url)
            cursor_values = query.get('cursor')

            if cursor_values:
                return cursor_values[0]
