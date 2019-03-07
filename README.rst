==============
Doomsday Clock
==============

.. image:: https://img.shields.io/github/release/renemarc/doomsday-clock/all.svg?logo=git&logoColor=white&maxAge=21600
        :target: https://github.com/renemarc/doomsday-clock
        :alt: Release

.. image:: https://img.shields.io/pypi/v/doomsday_clock.svg?logo=python&logoColor=White&maxAge=21600
        :target: https://pypi.python.org/pypi/doomsday_clock
        :alt: Python Package Index

.. image:: https://img.shields.io/travis/com/renemarc/doomsday-clock.svg?logo=travis-ci&logoColor=White
        :target: https://travis-ci.com/renemarc/doomsday-clock
        :alt: Travis CI

.. image:: https://img.shields.io/readthedocs/doomsday-clock.svg?logo=read-the-docs&logoColor=White&maxAge=21600
        :target: https://doomsday-clock.readthedocs.io/en/latest/
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/renemarc/doomsday_clock/shield.svg
        :target: https://pyup.io/repos/github/renemarc/doomsday_clock/
        :alt: Updates

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/ambv/black
        :alt: Code style: black

.. image:: https://img.shields.io/github/license/renemarc/doomsday-clock.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3LjgsMjBDMTcuNCwyMS4yIDE2LjMsMjIgMTUsMjJINUMzLjMsMjIgMiwyMC43IDIsMTlWMThINUwxNC4yLDE4QzE0LjYsMTkuMiAxNS43LDIwIDE3LDIwSDE3LjhNMTksMkMyMC43LDIgMjIsMy4zIDIyLDVWNkgyMFY1QzIwLDQuNCAxOS42LDQgMTksNEMxOC40LDQgMTgsNC40IDE4LDVWMThIMTdDMTYuNCwxOCAxNiwxNy42IDE2LDE3VjE2SDVWNUM1LDMuMyA2LjMsMiA4LDJIMTlNOCw2VjhIMTVWNkg4TTgsMTBWMTJIMTRWMTBIOFoiIGZpbGw9IiNmZmZmZmYiIC8+PC9zdmc+Cg==&maxAge=86400
        :target: ./LICENSE
        :alt: License

.. image:: https://img.shields.io/badge/pull_requests-welcome-brightgreen.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYsM0EzLDMgMCAwLDEgOSw2QzksNy4zMSA4LjE3LDguNDIgNyw4LjgzVjE1LjE3QzguMTcsMTUuNTggOSwxNi42OSA5LDE4QTMsMyAwIDAsMSA2LDIxQTMsMyAwIDAsMSAzLDE4QzMsMTYuNjkgMy44MywxNS41OCA1LDE1LjE3VjguODNDMy44Myw4LjQyIDMsNy4zMSAzLDZBMywzIDAgMCwxIDYsM002LDVBMSwxIDAgMCwwIDUsNkExLDEgMCAwLDAgNiw3QTEsMSAwIDAsMCA3LDZBMSwxIDAgMCwwIDYsNU02LDE3QTEsMSAwIDAsMCA1LDE4QTEsMSAwIDAsMCA2LDE5QTEsMSAwIDAsMCA3LDE4QTEsMSAwIDAsMCA2LDE3TTIxLDE4QTMsMyAwIDAsMSAxOCwyMUEzLDMgMCAwLDEgMTUsMThDMTUsMTYuNjkgMTUuODMsMTUuNTggMTcsMTUuMTdWN0gxNVYxMC4yNUwxMC43NSw2TDE1LDEuNzVWNUgxN0EyLDIgMCAwLDEgMTksN1YxNS4xN0MyMC4xNywxNS41OCAyMSwxNi42OSAyMSwxOE0xOCwxN0ExLDEgMCAwLDAgMTcsMThBMSwxIDAgMCwwIDE4LDE5QTEsMSAwIDAsMCAxOSwxOEExLDEgMCAwLDAgMTgsMTdaIiBmaWxsPSIjZmZmZmZmIiAvPjwvc3ZnPgo=&maxAge=86400
        :target: http://makeapullrequest.com
        :alt: PRs welcome

.. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&maxAge=86400
        :target: https://twitter.com/intent/tweet?text=Doomsday%20Clock%20client%20package%20for%20Python&url=https://github.com/renemarc/doomsday-clock&via=renemarc&hashtags=Radon,Airthings-Wave,MQTT,balena,Docker,RaspberryPi,IoT,SmartHome
        :alt: Twitter



Fetch the current `Doomsday Clock`_ world threat assessment from `TheBulletin.org`_.


* Free software: MIT license
* Documentation: https://doomsday-clock.readthedocs.io


Features
--------

* Fetches the current `Doomsday Clock`_ world threat assessment from `TheBulletin.org`_.
* Converts the Doomsday Clock sentence into countdown (1 minute), clock (11:59), and time (23:59:00).
* Offers a command-line interface.
* Uses async IO.
* Python 3.5+ compatible.
* Complete code coverage.

.. _Doomsday Clock: https://thebulletin.org/doomsday-clock/
.. _TheBulletin.org: https://thebulletin.org/


Credits
-------

* The `Bulletin of the Atomic Scientists`_ for keeping the world in check since 1947.
* `Matt Bierner`_ for the inspiration from his MinutesToMidnight_ Node.js library.
* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Bulletin of the Atomic Scientists: https://thebulletin.org/doomsday-clock/past-statements/
.. _Matt Bierner: https://github.com/mattbierner
.. _MinutesToMidnight: https://github.com/mattbierner/MinutesToMidnight
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
