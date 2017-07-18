from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pybutton.resources import Accounts
from pybutton.resources import Customers
from pybutton.resources import Merchants
from pybutton.resources import Orders
from pybutton.error import ButtonClientError


class Client(object):
    '''Top-level interface for making requests to the Button API.

    All resources implemented in this client will be exposed as attributes of a
    pybutton.Client instance.

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
            api_version: A specific API version label to use for the request

    Attributes:
        orders (pybutton.Resource): Resource for managing Button Orders.

    Raises:
        pybutton.ButtonClientError

    '''

    def __init__(self, api_key, config=None):

        if not api_key:
            raise ButtonClientError((
                'Must provide a Button API key.  Find yours at'
                ' https://app.usebutton.com/settings/organization'
            ))

        if config is None:
            config = {}

        config = config_with_defaults(config)

        self.orders = Orders(api_key, config)
        self.accounts = Accounts(api_key, config)
        self.merchants = Merchants(api_key, config)
        self.customers = Customers(api_key, config)


def config_with_defaults(config):
    secure = config.get('secure', True)
    defaultPort = 443 if secure else 80

    return {
        'secure': secure,
        'timeout': config.get('timeout'),
        'hostname': config.get('hostname', 'api.usebutton.com'),
        'port': config.get('port', defaultPort),
        'api_version': config.get('api_version'),
    }
