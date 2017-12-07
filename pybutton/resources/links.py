from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pybutton.resources.resource import Resource


class Links(Resource):
    '''Manages interacting with Button Links via the Button API

    See Resource for class docstring.

    '''

    def _path(self):
        '''Format a url path

        Args:
            link (dict): A dict representing the attributes of a link

        Returns:
            (str): The formatted path

        '''

        return '/v1/links'

    def create(self, link):
        '''Create a link

        Args:
            link (dict): A dict representing the attributes of a link

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        return self.api_post(self._path(), link)

    def get_info(self, link):
        '''Get info on a link

        Args:
            link (dict): A dict representing the attributes of a link for info

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        return self.api_post(self._path() + '/info', link)
