=====
Usage
=====

To use Countdoom in a project::

    import countdoom


.. literalinclude:: ../examples/example.py
   :language: python
   :lines: 6-21
   :linenos:


.. literalinclude:: ../examples/example.py
   :language: python
   :lines: 5-10,24-32
   :linenos:

The `Doomsday Clock`_ doesn't change often, at most once a year, and offers no
API. Since this package relies on web scraping of `TheBulletin.org`_, do
consider throttling/caching your requests.

.. _Doomsday Clock: https://thebulletin.org/doomsday-clock/
.. _TheBulletin.org: https://thebulletin.org/
