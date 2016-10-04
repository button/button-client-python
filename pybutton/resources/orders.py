from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .resource import Resource


class Orders(Resource):
    '''Manages interacting with Button Orders with the Button API

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

    '''

    def _path(self, order_id=None):
        '''Format a url path

        Args:
            order_id (str) optional: A Button order id ('btnorder-XXX')

        Returns:
            (str): The formatted path

        '''

        if order_id:
            return '/v1/order/{0}'.format(order_id)
        else:
            return '/v1/order'

    def get(self, order_id):
        '''Get an order

        Args:
            order_id (str) : A Button order id ('btnorder-XXX')

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        return self.api_get(self._path(order_id))

    def create(self, order):
        '''Create an order

        Args:
            order (dict): A dict representing the attributes of an order

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        return self.api_post(self._path(), order)

    def update(self, order_id, order):
        '''Update an order

        Args:
            order_id (str) : A Button order id ('btnorder-XXX')
            order (dict): A dict representing the attributes of an order

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        return self.api_post(self._path(order_id), order)

    def delete(self, order_id):
        '''Delete an order

        Args:
            order_id (str) : A Button order id ('btnorder-XXX')

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        return self.api_delete(self._path(order_id))
