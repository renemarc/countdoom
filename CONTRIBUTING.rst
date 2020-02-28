============
Contributing
============

Contributions are welcome, and they are greatly appreciated! 😃 Every little bit
helps, and `credit will always be given
<https://github.com/renemarc/countdoom#contributors->`_. ✨

You can contribute in many ways:

Types of contributions
----------------------

Report bugs
~~~~~~~~~~~

Please report bugs at https://github.com/renemarc/countdoom/issues.

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

**Note:** While |Countdoom| runs on Python 3.5+, dev tools require Python 3.6+
to run.

1. Fork the |Countdoom| `repo on GitHub <https://github.com/renemarc/countdoom/>`_.
2. Clone your fork locally:

  .. code-block:: console

    $ git clone git@github.com:YOUR_USERNAME_HERE/countdoom.git

3. Create a `virtual environment
<https://docs.python.org/3/tutorial/venv.html>`_ for local development:

  .. code-block:: console

    $ cd countdoom/
    $ python -m venv .venv
    $ . .venv/bin/activate

4. Install your local copy with all dependencies using pip:

  .. code-block:: console

        $ pip install -e .[dev]

  Alternatively, you can also use ``setup.py`` to install the above requirements:

  .. code-block:: console

        $ pip install --upgrade setuptools
        $ python setup.py develop

5. Create a branch for local development:

  .. code-block:: console

        $ git checkout -b name-of-your-bugfix-or-feature

  Now you can make your changes locally!

6. When you're done making changes, you can test the results with `makefile
<https://www.gnu.org/software/make/manual/make.html>`_. This will verify that
your changes pass `flake8 <https://flake8.pycqa.org/>`_ and the `tests
<https://docs.pytest.org/en/latest/>`_, including testing other
Python versions with `tox <https://tox.readthedocs.io/>`_:

  .. code-block:: console

        $ make test-all
        $ make coverage

  Alternatively, you can run the test suites individually:

  .. code-block:: console

        $ flake8 countdoom tests
        $ pytest
        $ tox -em py35
        $ tox -em py36
        $ tox -em py37
        $ tox -em py38
        $ coverage

7. Commit your changes using `Conventional Commits
<https://www.conventionalcommits.org/>`_ style and push your branch to GitHub:

  .. code-block:: console

        $ git add .
        $ git commit -m "type(scope): detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

8. `Submit a pull request
<https://github.com/renemarc/countdoom/pulls>`_ through the GitHub website.

Pull request guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in ``README.md`` (repo) and ``README.rst`` (docs).
3. The pull request should work for Python 3.5, 3.6, 3.7, 3.8, and for PyPy.
   Check https://travis-ci.com/renemarc/countdoom/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests:

.. code-block:: console

    $ pytest tests.test_countdoom


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in `HISTORY.rst
<https://github.com/renemarc/countdoom/blob/master/HISTORY.rst>`_).
Then run:

.. code-block:: console

    $ bumpversion patch # possible: major / minor / patch
    $ git push
    $ git push --tags

`Travis CI <https://travis-ci.com/renemarc/countdoom>`__ will then deploy to
the `Python Package Index <https://pypi.org/project/countdoom/>`__ if tests pass.

.. _GitHub issues: https://github.com/renemarc/countdoom/issues


.. |Countdoom| replace:: **Countdoom**
