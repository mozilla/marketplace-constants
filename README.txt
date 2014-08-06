Global constants for the Firefox Marketplace, available in both JS and Python.

Python
------

Example::

    >>> from mpconstants import payments
    >>> payments.PAYMENT_STATUSES
    {1: 'passed', 2: 'failed'}

Node
----

Example::

    > var c = require('./mpconstants.js')
    > c('payments')['PAYMENT_STATUSES']
      { '1': 'passed',
        '2': 'failed' }
