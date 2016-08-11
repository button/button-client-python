from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .resources import Orders
from .error import ButtonClientError


class Client(object):
    '''Top-level interface for making requests to the Button API.

    All resources implemented in this client will be exposed as attributes of a
    pybutton.Client instance.

    Args:
        api_key (string): Your organization's API key.  Do find yours at
            https://app.usebutton.com/settings/organization.

    Attributes:
        orders (pybutton.Resource): Resource for managing Button Orders.

    Raises:
        pybutton.ButtonClientError

    '''

    def __init__(self, api_key):

        if not api_key:
            raise ButtonClientError((
                'Must provide a Button API key.  Find yours at'
                ' https://app.usebutton.com/settings/organization'
            ))

        self.orders = Orders(api_key)
