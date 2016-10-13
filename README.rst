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

Configuration
-------------

You may optionally supply a config argument with your API key:

.. code:: python

  from pybutton import Client

  client = Client("sk-XXX", {
    'hostname': 'api.testsite.com',
    'port': 80,
    'secure': False,
    'timeout': 5, # seconds
  })

The supported options are as follows:

* ``hostname``: Defaults to ``api.usebutton.com``.
* ``port``: Defaults to ``443`` if ``config.secure``, else defaults to ``80``.
* ``secure``: Whether or not to use HTTPS.  Defaults to ``True``.  **N.B: Button's API is only exposed through HTTPS.  This option is provided purely as a convenience for testing and development.**
* ``timeout``: The time in seconds that may elapse before network requests abort.  Defaults to ``None``.

Resources
---------

We currently expose two resources to manage, ``Orders`` and ``Accounts``.

Orders
~~~~~~

**n.b: all currency values should be reported in the smallest possible
unit of that denomination, i.e. $1.00 should be reported as 100
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

Accounts
~~~~~~~~

All
'''

.. code:: python

    from pybutton import Client

    client = Client('sk-XXX')

    response = client.accounts.all()

    print(response)
    # <class pybutton.Response [2 elements]>

Transactions
''''''''''''

Along with the required account ID, you may also
pass the following optional arguments:

* ``cursor`` (string): An API cursor to fetch a specific set of results.
* ``start`` (ISO-8601 datetime string): Fetch transactions after this time.
* ``end`` (ISO-8601 datetime string): Fetch transactions before this time.

.. code:: python

    from pybutton import Client

    client = Client('sk-XXX')

    response = client.accounts.transactions(
        'acc-123',
        start='2016-07-15T00:00:00.000Z',
        end='2016-09-30T00:00:00.000Z'
    )

    print(response)
    # <class pybutton.Response [100 elements]>

Response
--------

Methods
~~~~~~~

data
''''

.. code:: python

    from pybutton import Client

    client = Client('sk-XXX')

    response = client.orders.get('btnorder-XXX')

    print(response.data())
    # {'total': 50, 'currency': 'USD', 'status': 'open' ... }

    response = client.accounts.all()

    print(response.data())
    # [{'id': 'acc-123', ... }, {'id': 'acc-234', ... }]

next_cursor
''''''''''

For any paged resource, ``next_cursor()`` will return a cursor to
supply for the next page of results. If ``next_cursor()`` returns ``None``,
there are no more results.

.. code:: python

    from pybutton import Client

    client = Client('sk-XXX')

    response = client.accounts.transactions('acc-123')
    cursor = response.next_cursor()

    # loop through and print all transactions
    while cursor:
        response = client.accounts.transactions('acc-123', cursor=cursor)
        print(response.data())
        cursor = response.next_cursor()

prev_cursor
''''''''''

For any paged resource, ``prev_cursor()`` will return a cursor to
supply for the next page of results. If ``prev_cursor()`` returns
``None``, there are no more previous results.

.. code:: python

    from pybutton import Client

    client = Client('sk-XXX')

    response = client.accounts.transactions('acc-123', cursor='xyz')

    print(response)
    # <class pybutton.Response [25 elements]>

    cursor = response.prev_cursor()

    response = client.accounts.transactions('acc-123', cursor=cursor)

    print(response)
    # <class pybutton.Response [100 elements]>


Contributing
------------

-  Building the egg: ``python setup.py bdist_egg``
-  Building the wheel: ``python setup.py bdist_wheel --universal``
-  Building the sdist: ``python setup.py sdist``
-  Installing locally: ``python setup.py install``
-  Running tests: ``python setup.py test``
-  Running lint: ``flake8``

.. |Build Status| image:: https://travis-ci.org/button/button-client-python.svg?branch=master
   :target: https://travis-ci.com/button/button-client-python
