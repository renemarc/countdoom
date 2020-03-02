=====
Usage
=====

.. _cli:

Command-line interface
----------------------

Example usage:

.. code-block:: console

    $ countdoom

     11 12   ️
    10 \|      Countdoom: Doomsday Clock 🤯 🌊 ☢️ ☠️
    9   @      World threat assessment from TheBulletin.org

     Sentence: IT IS 2 MINUTES TO MIDNIGHT
        Clock: 11:58
         Time: 23:58:00
      Minutes: 2
      Seconds: 120
    Countdown: 120 seconds


Example usage using a single format (e.g. clock):

.. code-block:: console

    $ countdoom --format clock

    11:58


Built-in help:

.. code-block:: console

    $ countdoom -h

     11 12   ️
    10 \|      Countdoom: Doomsday Clock 🤯 🌊 ☢️ ☠️
    9   @      World threat assessment from TheBulletin.org

    usage: countdoom [--format {sentence,clock,time,minutes,countdown,all,json}]
                     [--timeout TIMEOUT] [--v] [-h]

    optional arguments:
      --format {sentence,clock,time,countdown,all,json}
                            return data format (default: all).
      --timeout TIMEOUT     connection/request timeout in seconds (default: 10).
      --v, --version        show program's version number and exit
      -h, --help            show this help message and exit

    "Be the change you want to see in the world." —Gandhi/Arleen Lorrance


Python import
-------------

To use |Countdoom| in a project:

.. code-block:: python

    import countdoom


Get the current Doomsday Clock value using the event loop:

.. literalinclude:: ../examples/example.py
   :language: python
   :lines: 5-21
   :linenos:


Get the current Doomsday Clock value using an awaitable:

.. literalinclude:: ../examples/example.py
   :language: python
   :lines: 6-10,24-32
   :linenos:


Notes
-----

The `Doomsday Clock`_ doesn't change often, at most once a year, and offers no
API. Since this package relies on web scraping of `TheBulletin.org`_, do
consider throttling/caching your requests.

.. _Doomsday Clock: https://thebulletin.org/doomsday-clock/
.. _TheBulletin.org: https://thebulletin.org/

.. |Countdoom| replace:: **Countdoom**
