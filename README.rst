########################################
🤯 Countdoom: a Doomsday Clock client 🕚
########################################

|badge-release| |badge-price| |badge-pypi| |badge-python| |badge-travis| |badge-docs| |badge-codecov| |badge-codeclimate-maintain| |badge-codefactor| |badge-black| |badge-license| |badge-codetriage| |badge-contributors| |badge-contribute| |badge-twitter|

Python package to fetch and digest the current `Doomsday Clock`_ world threat
assessment from `TheBulletin.org <https://thebulletin.org/>`__.

.. figure:: https://github.com/renemarc/countdoom/blob/master/docs/screenshot.png?raw=true
        :align: center
        :alt: Command-line interface output
        :figclass: align-center

        *Countdoom: a Doomsday Clock client.*

* Free software: `MIT license <https://github.com/renemarc/countdoom/blob/master/LICENSE>`_
* Documentation: `Read the Docs <https://countdoom.readthedocs.io/>`_
* Source code: `GitHub <https://github.com/renemarc/countdoom/>`_
* Python package: `PyPI <https://pypi.org/project/countdoom/>`_


********
Features
********

* Fetches the current `Doomsday Clock`_ value from the
  `Bulletin of the Atomic Scientists`_.
* Converts the Doomsday Clock sentence into countdown seconds ``60``, countdown
  minutes ``1``, clock ``11:59``, and time ``23:59:00``.
* Offers a command-line interface.
* Uses async IO.
* Python 3.5+ compatible.
* Complete code coverage.


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

.. |badge-codetriage| image:: https://www.codetriage.com/renemarc/countdoom/badges/users.svg
        :target: https://www.codetriage.com/renemarc/countdoom
        :alt: CodeFactor rating

.. |badge-contribute| image:: https://img.shields.io/badge/pull_requests-welcome-brightgreen.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYsM0EzLDMgMCAwLDEgOSw2QzksNy4zMSA4LjE3LDguNDIgNyw4LjgzVjE1LjE3QzguMTcsMTUuNTggOSwxNi42OSA5LDE4QTMsMyAwIDAsMSA2LDIxQTMsMyAwIDAsMSAzLDE4QzMsMTYuNjkgMy44MywxNS41OCA1LDE1LjE3VjguODNDMy44Myw4LjQyIDMsNy4zMSAzLDZBMywzIDAgMCwxIDYsM002LDVBMSwxIDAgMCwwIDUsNkExLDEgMCAwLDAgNiw3QTEsMSAwIDAsMCA3LDZBMSwxIDAgMCwwIDYsNU02LDE3QTEsMSAwIDAsMCA1LDE4QTEsMSAwIDAsMCA2LDE5QTEsMSAwIDAsMCA3LDE4QTEsMSAwIDAsMCA2LDE3TTIxLDE4QTMsMyAwIDAsMSAxOCwyMUEzLDMgMCAwLDEgMTUsMThDMTUsMTYuNjkgMTUuODMsMTUuNTggMTcsMTUuMTdWN0gxNVYxMC4yNUwxMC43NSw2TDE1LDEuNzVWNUgxN0EyLDIgMCAwLDEgMTksN1YxNS4xN0MyMC4xNywxNS41OCAyMSwxNi42OSAyMSwxOE0xOCwxN0ExLDEgMCAwLDAgMTcsMThBMSwxIDAgMCwwIDE4LDE5QTEsMSAwIDAsMCAxOSwxOEExLDEgMCAwLDAgMTgsMTdaIiBmaWxsPSIjZmZmZmZmIiAvPjwvc3ZnPgo=&cacheSeconds=86400
        :target: https://countdoom.readthedocs.io/en/latest/contributing.html
        :alt: PRs welcome

.. |badge-contributors| image:: https://img.shields.io/badge/all_contributors-welcome-orange.svg?logo=github
        :target: https://countdoom.readthedocs.io/en/latest/authors.html
        :alt: All Contributors

.. |badge-docs| image:: https://img.shields.io/readthedocs/countdoom.svg?logo=read-the-docs&logoColor=White&cacheSeconds=21600
        :target: https://countdoom.readthedocs.io/en/latest/
        :alt: Documentation Status

.. |badge-license| image:: https://img.shields.io/github/license/renemarc/countdoom.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3LjgsMjBDMTcuNCwyMS4yIDE2LjMsMjIgMTUsMjJINUMzLjMsMjIgMiwyMC43IDIsMTlWMThINUwxNC4yLDE4QzE0LjYsMTkuMiAxNS43LDIwIDE3LDIwSDE3LjhNMTksMkMyMC43LDIgMjIsMy4zIDIyLDVWNkgyMFY1QzIwLDQuNCAxOS42LDQgMTksNEMxOC40LDQgMTgsNC40IDE4LDVWMThIMTdDMTYuNCwxOCAxNiwxNy42IDE2LDE3VjE2SDVWNUM1LDMuMyA2LjMsMiA4LDJIMTlNOCw2VjhIMTVWNkg4TTgsMTBWMTJIMTRWMTBIOFoiIGZpbGw9IiNmZmZmZmYiIC8+PC9zdmc+Cg==&cacheSeconds=86400
        :target: https://github.com/renemarc/countdoom/blob/master/LICENSE
        :alt: License

.. |badge-price| image:: https://img.shields.io/badge/FREE_as_in-SPEECH-success.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0xNS40MSwyMkMxNS4zNSwyMiAxNS4yOCwyMiAxNS4yMiwyMkMxNS4xLDIxLjk1IDE1LDIxLjg1IDE0Ljk2LDIxLjczTDEyLjc0LDE1LjkzQzEyLjY1LDE1LjY5IDEyLjc3LDE1LjQyIDEzLDE1LjMyQzEzLjcxLDE1LjA2IDE0LjI4LDE0LjUgMTQuNTgsMTMuODNDMTUuMjIsMTIuNCAxNC41OCwxMC43MyAxMy4xNSwxMC4wOUMxMS43Miw5LjQ1IDEwLjA1LDEwLjA5IDkuNDEsMTEuNUM5LjExLDEyLjIxIDkuMDksMTMgOS4zNiwxMy42OUM5LjY2LDE0LjQzIDEwLjI1LDE1IDExLDE1LjI4QzExLjI0LDE1LjM3IDExLjM3LDE1LjY0IDExLjI4LDE1Ljg5TDksMjEuNjlDOC45NiwyMS44MSA4Ljg3LDIxLjkxIDguNzUsMjEuOTZDOC42MywyMiA4LjUsMjIgOC4zOSwyMS45NkMzLjI0LDE5Ljk3IDAuNjcsMTQuMTggMi42Niw5LjAzQzQuNjUsMy44OCAxMC40NCwxLjMxIDE1LjU5LDMuM0MxOC4wNiw0LjI2IDIwLjA1LDYuMTUgMjEuMTMsOC41N0MyMi4yMiwxMSAyMi4yOSwxMy43NSAyMS4zMywxNi4yMkMyMC4zMiwxOC44OCAxOC4yMywyMSAxNS41OCwyMkMxNS41LDIyIDE1LjQ3LDIyIDE1LjQxLDIyTTEyLDMuNTlDNy4wMywzLjQ2IDIuOSw3LjM5IDIuNzcsMTIuMzZDMi42OCwxNi4wOCA0Ljg4LDE5LjQ3IDguMzIsMjAuOUwxMC4yMSwxNkM4LjM4LDE1IDcuNjksMTIuNzIgOC42OCwxMC44OUM5LjY3LDkuMDYgMTEuOTYsOC4zOCAxMy43OSw5LjM2QzE1LjYyLDEwLjM1IDE2LjMxLDEyLjY0IDE1LjMyLDE0LjQ3QzE0Ljk3LDE1LjEyIDE0LjQ0LDE1LjY1IDEzLjc5LDE2TDE1LjY4LDIwLjkzQzE3Ljg2LDE5Ljk1IDE5LjU3LDE4LjE2IDIwLjQ0LDE1LjkzQzIyLjI4LDExLjMxIDIwLjA0LDYuMDggMTUuNDIsNC4yM0MxNC4zMywzLjggMTMuMTcsMy41OCAxMiwzLjU5WiIgLz4KPC9zdmc+&cacheSeconds=86400
        :target: https://github.com/renemarc/countdoom/
        :alt: Price

.. |badge-pypi| image:: https://img.shields.io/pypi/v/countdoom.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0yMSwxNi41QzIxLDE2Ljg4IDIwLjc5LDE3LjIxIDIwLjQ3LDE3LjM4TDEyLjU3LDIxLjgyQzEyLjQxLDIxLjk0IDEyLjIxLDIyIDEyLDIyQzExLjc5LDIyIDExLjU5LDIxLjk0IDExLjQzLDIxLjgyTDMuNTMsMTcuMzhDMy4yMSwxNy4yMSAzLDE2Ljg4IDMsMTYuNVY3LjVDMyw3LjEyIDMuMjEsNi43OSAzLjUzLDYuNjJMMTEuNDMsMi4xOEMxMS41OSwyLjA2IDExLjc5LDIgMTIsMkMxMi4yMSwyIDEyLjQxLDIuMDYgMTIuNTcsMi4xOEwyMC40Nyw2LjYyQzIwLjc5LDYuNzkgMjEsNy4xMiAyMSw3LjVWMTYuNU0xMiw0LjE1TDYuMDQsNy41TDEyLDEwLjg1TDE3Ljk2LDcuNUwxMiw0LjE1TTUsMTUuOTFMMTEsMTkuMjlWMTIuNThMNSw5LjIxVjE1LjkxTTE5LDE1LjkxVjkuMjFMMTMsMTIuNThWMTkuMjlMMTksMTUuOTFaIiAvPgo8L3N2Zz4=&cacheSeconds=86400
        :target: https://pypi.org/project/countdoom/
        :alt: Python Package Index

.. |badge-python| image:: https://img.shields.io/pypi/pyversions/countdoom.svg?logo=python&logoColor=White&cacheSeconds=21600
        :target: https://pypi.python.org/pypi/countdoom
        :alt: Python Versions

.. |badge-release| image:: https://img.shields.io/github/release/renemarc/countdoom/all.svg?logo=git&logoColor=white&cacheSeconds=21600
        :target: https://github.com/renemarc/countdoom/releases/latest
        :alt: Release

.. |badge-travis| image:: https://img.shields.io/travis/com/renemarc/countdoom.svg?logo=travis-ci&logoColor=White
        :target: https://travis-ci.com/renemarc/countdoom
        :alt: Travis CI

.. |badge-twitter| image:: https://img.shields.io/twitter/url/https/github.com/renemarc/countdoom.svg?style=social&cacheSeconds=86400
        :target: https://twitter.com/intent/tweet?text=Countdoom%3A%20a%20%23DoomsdayClock%20client%20package%20for%20%23Python%21&via=renemarc&hashtags=Doomsday,BulletinAtomic
        :alt: Twitter


.. _Bulletin of the Atomic Scientists: https://thebulletin.org/
.. _Doomsday Clock: https://thebulletin.org/doomsday-clock/
