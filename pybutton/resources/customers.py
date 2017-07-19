from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pybutton.resources.resource import Resource


class Customers(Resource):
    '''Manages interacting with Button Customers via the Button API

    See Resource for class docstring.

    '''

    def _path(self, customer_id=None):
        '''Format a url path

        Args:
            customer_id (str) optional: A Button customer id ('customer-XXX')

        Returns:
            (str): The formatted path

        '''

        if customer_id:
            return '/v1/customers/{0}'.format(customer_id)
        else:
            return '/v1/customers'

    def get(self, customer_id):
        '''Get a customer

        Args:
            customer_id (str) : A Button customer id ('customer-XXX')

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        return self.api_get(self._path(customer_id))

    def create(self, customer):
        '''Create an customer

        Args:
            customer (dict): A dict representing the attributes of an customer

        Raises:
            pybutton.ButtonClientError

        Returns:
            (pybutton.Response) The API response

        '''

        return self.api_post(self._path(), customer)
