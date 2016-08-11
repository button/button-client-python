button-client-python |Build Status|
===================================

This module is a thin client for interacting with Button's API.

Please see the full `API
Docs <https://www.usebutton.com/developers/api-reference>`__ for more
information. For help, check out our
`Support <https://www.usebutton.com/support>`__ page or `get in
touch <https://www.usebutton.com/contact>`__.

Supported runtimes
^^^^^^^^^^^^^^^^^^

-  cPython ``2.6``, ``2.7``, ``3.2``, ``3.3``, ``3.4``, ``3.5``

Dependencies
^^^^^^^^^^^^

-  None

Usage
-----

.. code:: bash

    pip install pybutton

To create a client capable of making network requests, instantiate a
``pybutton.Client`` with your `API
key <https://app.usebutton.com/settings/organization>`__.

.. code:: python

    from pybutton import Client

    client = Client('sk-XXX')

The client will always attempt to raise a ``pybutton.ButtonClientError``
in an error condition.

All API requests will return a ``pybutton.response.Response`` instance,
which supports accessing data properties from the API response as
attributes. To access the raw response dict, use ``#to_dict``. For
instance:

.. code:: python

    from pybutton import Client
    from pybutton import ButtonClientError

    client = Client("sk-XXX")

    try:
        response = client.orders.get("btnorder-XXX")
    except ButtonClientError as e:
        print(e)

    print(response)
    # <class pybutton.Response status: open, btn_ref: None, line_items: [], ...>

    print(response.status)
    # 'open'

    print(response.to_dict())
    # {'status': open, 'btn_ref': None, 'line_items': [], ...}

Resources
---------

We currently expose only one resource to manage, ``Orders``.

Orders
~~~~~~

**n.b: all currency values should be reported in the smallest possible
unit of that denomination, i.e. $1.00 should be reported as ``100``
(i.e. 100 pennies)**

Create
''''''

.. code:: python

    from pybutton import Client

    client = Client('sk-XXX')

    response = client.orders.create({
        'total': 50,
        'currency': 'USD',
        'order_id': '2007',
        'finalization_date': '2017-08-02T19:26:08Z',
    })

    print(response)
    # <class pybutton.Response total: 50, currency: 'USD', ...>

Get
'''

.. code:: python

    from pybutton import Client

    client = Client('sk-XXX')

    response = client.orders.get('btnorder-XXX')

    print(response)
    # <class pybutton.Response total: 50, currency: 'USD', ...>

Update
''''''

.. code:: python

    from pybutton import Client

    client = Client('sk-XXX')

    response = client.orders.update('btnorder-XXX', {
        'total': 60,
    })

    print(response)
    # <class pybutton.Response total: 60, currency: 'USD', ...>

Delete
''''''

.. code:: python

    from pybutton import Client

    client = Client('sk-XXX')

    response = client.orders.delete('btnorder-XXX')

    print(response)
    # <class pybutton.Response >

Contributing
------------

-  Building the egg: ``python setup.py bdist_egg``
-  Installing locally: ``python setup.py install``
-  Running tests: ``python setup.py test``
-  Running lint: ``flake8``

.. |Build Status| image:: https://travis-ci.org/button/button-client-python.svg?branch=master
   :target: https://travis-ci.com/button/button-client-python
