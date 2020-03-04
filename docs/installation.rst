.. highlight:: shell

============
Installation
============

Stable release |badge-pypi| |badge-python| |badge-wheel|
--------------------------------------------------------

|Countdoom| is distributed on the `Python Package Index (PyPI)
<https://pypi.org/project/countdoom/>`_. The best way to install it is with
`pip <https://packaging.python.org/tutorials/installing-packages/>`__:

(Optional) Create a virtual environment:

.. code-block:: console

    $ virtualenv countdoom-env

To install |Countdoom|, run this command in your terminal:

.. code-block:: console

    $ pip install countdoom

This is the preferred method to install |Countdoom|, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.


From sources |badge-github| |badge-release|
-------------------------------------------

The sources for |Countdoom| can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/renemarc/countdoom

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/renemarc/countdoom/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

Or if you're on a system that supports makefiles:

.. code-block:: console

    $ make install


.. _Github repo: https://github.com/renemarc/countdoom
.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/
.. _tarball: https://github.com/renemarc/countdoom/tarball/master


.. |badge-github| image:: https://img.shields.io/badge/fork_me_on-GitHub-blue?logo=github&logoColor=white&cacheSeconds=86400
        :target: https://github.com/renemarc/countdoom
        :alt: GitHub

.. |badge-pypi| image:: https://img.shields.io/pypi/v/countdoom.svg?logo=pypi&logoColor=White&cacheSeconds=21600
        :target: https://pypi.org/project/countdoom/
        :alt: Python Package Index

.. |badge-python| image:: https://img.shields.io/pypi/pyversions/countdoom.svg?logo=python&logoColor=White&cacheSeconds=21600
        :target: https://pypi.python.org/pypi/countdoom
        :alt: Python versions

.. |badge-release| image:: https://img.shields.io/github/release/renemarc/countdoom/all.svg?logo=git&logoColor=white&cacheSeconds=21600
        :target: https://github.com/renemarc/countdoom/releases/latest
        :alt: Release

.. |badge-wheel| image:: https://img.shields.io/pypi/wheel/countdoom.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0xMiwyQTEwLDEwIDAgMCwwIDIsMTJBMTAsMTAgMCAwLDAgMTIsMjJBMTAsMTAgMCAwLDAgMjIsMTJBMTAsMTAgMCAwLDAgMTIsMk0xMiw5QTMsMyAwIDAsMSAxNSwxMkEzLDMgMCAwLDEgMTIsMTVBMywzIDAgMCwxIDksMTJBMywzIDAgMCwxIDEyLDlaIiAvPgo8L3N2Zz4=&cacheSeconds=86400
        :target: https://pypi.org/project/countdoom/#files
        :alt: Python wheel

.. |Countdoom| replace:: **Countdoom**
