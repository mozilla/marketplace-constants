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

The content of these files are generated from multiple sources:

* Python code copied out of the various marketplace repositories
* JSON code pulled from the Mozilla SVN servers

If you want to update any constants from SVN, or add in any new constants, then
run the generate script to build out the new files. Compare the differences,
add or remove any files from git and commit. To run the generate script::

    python generate.py


Bower
-----

```bower install marketplace-constants```

The package will consist of a directory of JSON files that you can pull and
require into your project.


**This package is on:**

* pypi: https://pypi.python.org/pypi/marketplace-constants
* npm: http://npmjs.org/package/marketplace-constants
* bower: bower install marketplace-constants
