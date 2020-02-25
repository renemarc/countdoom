============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and `credit will always be given
<https://github.com/renemarc/countdoom/blob/master/AUTHORS.md>`_.

You can contribute in many ways:

Types of contributions
----------------------

Report bugs
~~~~~~~~~~~

Report bugs at https://github.com/renemarc/countdoom/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix bugs
~~~~~~~~

Look through the `GitHub issues`_ for bugs. Anything tagged with ``bug`` and ``help
wanted`` is open to whoever wants to implement it.

Implement features
~~~~~~~~~~~~~~~~~~

Look through the `GitHub issues`_ for features. Anything tagged with ``enhancement``
and ``help wanted`` is open to whoever wants to implement it.

Write documentation
~~~~~~~~~~~~~~~~~~~

|Countdoom| could always use more documentation, whether as part of the official
|Countdoom| docs, in docstrings, or even on the web in blog posts, articles, and
such.

Submit feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/renemarc/countdoom/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome 😃

Get started!
------------

Ready to contribute? Here's how to set up |Countdoom| for local
development.

1. Fork the |Countdoom| `repo on GitHub <https://github.com/renemarc/countdoom/>`_.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/countdoom.git

3. Install your local copy into a virtualenv. Assuming you have
   `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/>`_ installed,
   this is how you set up your fork for local development::

    $ mkvirtualenv countdoom
    $ cd countdoom/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass
`flake8 <https://flake8.pycqa.org/>`_ and the `tests
<https://docs.pytest.org/en/latest/>`_, including testing other
Python versions with `tox <https://tox.readthedocs.io/>`_::

    $ flake8 countdoom tests
    $ python setup.py test or py.test
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. `Submit a pull request
<https://github.com/renemarc/countdoom/pulls>`_ through the GitHub website.

Pull request guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.5, 3.6, 3.7, 3.8, and for PyPy.
   Check https://travis-ci.com/renemarc/countdoom/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ py.test tests.test_countdoom


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in `HISTORY.rst
<https://github.com/renemarc/countdoom/blob/master/HISTORY.rst>`_).
Then run::

$ bumpversion patch # possible: major / minor / patch
$ git push
$ git push --tags

`Travis CI <https://travis-ci.com/renemarc/countdoom>`_ will then deploy to
`PyPI.org <https://pypi.org/project/countdoom/>`_ if tests pass.

.. _GitHub issues: https://github.com/renemarc/countdoom/issues


.. |Countdoom| replace:: **Countdoom**
