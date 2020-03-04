.. sidebar:: |badge-github| |badge-docs|

    |badge-python|
    |badge-pypi|
    |badge-wheel|

    |badge-contributors|
    |badge-license|


########################################################
🤯 Countdoom: a Doomsday Clock client 🕚 |badge-twitter|
########################################################

`Python package <https://pypi.org/project/countdoom/>`__ to fetch and digest the
current `Doomsday Clock`_ world threat assessment from `TheBulletin.org
<https://thebulletin.org/>`__.

Free software released under `MIT License`_, with source code available on
`GitHub`_, Python package distributed on `PyPI`_, and documentation hosted on
`Read the Docs`_.


**************************************************************************************
Features |badge-codecov| |badge-codeclimate-maintain| |badge-codefactor| |badge-black|
**************************************************************************************

* Fetches the current `Doomsday Clock`_ value from the `Bulletin of the Atomic
  Scientists`_.
* Converts the Doomsday Clock sentence into:

  * countdown seconds ``60``
  * countdown minutes ``1``
  * clock ``11:59``
  * time ``23:59:00``

* Offers a command-line interface.
* Uses `Async IO`_ for efficient Python integration.


.. figure:: https://github.com/renemarc/countdoom/blob/master/docs/screenshot.png?raw=true
        :align: center
        :alt: Command-line interface output
        :figclass: align-center

        *Countdoom: a Doomsday Clock client.*


.. |badge-black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0xMiwyQTEwLDEwIDAgMCwxIDIyLDEyQTEwLDEwIDAgMCwxIDEyLDIyQTEwLDEwIDAgMCwxIDIsMTJBMTAsMTAgMCAwLDEgMTIsMk0xNSwxMC41VjlBMiwyIDAgMCwwIDEzLDdIOVYxN0gxM0EyLDIgMCAwLDAgMTUsMTVWMTMuNUMxNSwxMi43IDE0LjMsMTIgMTMuNSwxMkMxNC4zLDEyIDE1LDExLjMgMTUsMTAuNU0xMywxNUgxMVYxM0gxM1YxNU0xMywxMUgxMVY5SDEzVjExWiIgLz4KPC9zdmc+&cacheSeconds=86400
        :target: https://black.readthedocs.io/
        :alt: Code style: black

.. |badge-codeclimate-maintain| image:: https://img.shields.io/codeclimate/maintainability/renemarc/countdoom.svg?logo=code-climate&cacheSeconds=300
        :target: https://codeclimate.com/github/renemarc/countdoom
        :alt: Code Climate maintainability

.. |badge-codecov| image:: https://img.shields.io/codecov/c/github/renemarc/countdoom?logo=codecov&logoColor=white&cacheSeconds=300
        :target: https://codecov.io/gh/renemarc/countdoom
        :alt: CodeCov coverage

.. |badge-codefactor| image:: https://img.shields.io/codefactor/grade/github/renemarc/countdoom?logo=codefactor&logoColor=white&cacheSeconds=300
        :target: https://www.codefactor.io/repository/github/renemarc/countdoom
        :alt: CodeFactor rating

.. |badge-contributors| image:: https://img.shields.io/badge/all_contributors-welcome-orange.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0xNiAxN1YxOUgyVjE3UzIgMTMgOSAxMyAxNiAxNyAxNiAxN00xMi41IDcuNUEzLjUgMy41IDAgMSAwIDkgMTFBMy41IDMuNSAwIDAgMCAxMi41IDcuNU0xNS45NCAxM0E1LjMyIDUuMzIgMCAwIDEgMTggMTdWMTlIMjJWMTdTMjIgMTMuMzcgMTUuOTQgMTNNMTUgNEEzLjM5IDMuMzkgMCAwIDAgMTMuMDcgNC41OUE1IDUgMCAwIDEgMTMuMDcgMTAuNDFBMy4zOSAzLjM5IDAgMCAwIDE1IDExQTMuNSAzLjUgMCAwIDAgMTUgNFoiIC8+Cjwvc3ZnPg==&cacheSeconds=21600
        :target: https://countdoom.readthedocs.io/en/latest/contributing.html
        :alt: All Contributors

.. |badge-docs| image:: https://img.shields.io/badge/-Read_the_Docs-blue?logo=read-the-docs&logoColor=white&cacheSeconds=86400
        :target: `Read the Docs`_
        :alt: Documentation at Read The Docs

.. |badge-github| image:: https://img.shields.io/badge/-Fork_me_on_GitHub-grey?logo=github&cacheSeconds=86400
        :target: `GitHub`_
        :alt: Fork me on GitHub

.. |badge-license| image:: https://img.shields.io/github/license/renemarc/countdoom.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3LjgsMjBDMTcuNCwyMS4yIDE2LjMsMjIgMTUsMjJINUMzLjMsMjIgMiwyMC43IDIsMTlWMThINUwxNC4yLDE4QzE0LjYsMTkuMiAxNS43LDIwIDE3LDIwSDE3LjhNMTksMkMyMC43LDIgMjIsMy4zIDIyLDVWNkgyMFY1QzIwLDQuNCAxOS42LDQgMTksNEMxOC40LDQgMTgsNC40IDE4LDVWMThIMTdDMTYuNCwxOCAxNiwxNy42IDE2LDE3VjE2SDVWNUM1LDMuMyA2LjMsMiA4LDJIMTlNOCw2VjhIMTVWNkg4TTgsMTBWMTJIMTRWMTBIOFoiIGZpbGw9IiNmZmZmZmYiIC8+PC9zdmc+Cg==&cacheSeconds=86400
        :target: `MIT License`_
        :alt: License

.. |badge-pypi| image:: https://img.shields.io/pypi/v/countdoom.svg?logo=pypi&logoColor=white&cacheSeconds=21600
        :target: `PyPI`_
        :alt: Python Package Index

.. |badge-python| image:: https://img.shields.io/pypi/pyversions/countdoom.svg?logo=python&logoColor=White&cacheSeconds=21600
        :target: https://pypi.python.org/pypi/countdoom
        :alt: Python Versions

.. |badge-twitter| image:: https://img.shields.io/twitter/url/https/github.com/renemarc/countdoom.svg?style=social&cacheSeconds=86400
        :target: https://twitter.com/intent/tweet?text=Countdoom%3A%20a%20%23DoomsdayClock%20client%20package%20for%20%23Python%21&via=renemarc&hashtags=Doomsday,BulletinAtomic
        :alt: Twitter

.. |badge-wheel| image:: https://img.shields.io/pypi/wheel/countdoom.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0xMiwyQTEwLDEwIDAgMCwwIDIsMTJBMTAsMTAgMCAwLDAgMTIsMjJBMTAsMTAgMCAwLDAgMjIsMTJBMTAsMTAgMCAwLDAgMTIsMk0xMiw5QTMsMyAwIDAsMSAxNSwxMkEzLDMgMCAwLDEgMTIsMTVBMywzIDAgMCwxIDksMTJBMywzIDAgMCwxIDEyLDlaIiAvPgo8L3N2Zz4=&cacheSeconds=86400
        :target: https://pypi.org/project/countdoom/#files
        :alt: Python wheel

.. _Async IO: https://docs.python.org/3/library/asyncio.html
.. _Bulletin of the Atomic Scientists: https://thebulletin.org/
.. _Doomsday Clock: https://thebulletin.org/doomsday-clock/
.. _GitHub: https://github.com/renemarc/countdoom/
.. _MIT License: https://github.com/renemarc/countdoom/blob/master/LICENSE
.. _PyPI: https://pypi.org/project/countdoom/
.. _Read the Docs: https://countdoom.readthedocs.io/
