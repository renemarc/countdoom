============================================
Contributing |badge-conduct| |badge-license|
============================================

Contributions are welcome, and they are greatly appreciated! 😃 This project
follows the `all-contributors`_ specification: every little bit helps and
`credit will always be given
<https://github.com/renemarc/countdoom#contributors->`_. ✨

.. note::

    This project is released with a respect oriented `Contributor Code of
    Conduct`_ based on the `Contributor Covenant`_. By participating in this
    project you agree to abide by its fair terms.

You can contribute in many ways:


Types of contributions |badge-contributors| |badge-issues|
----------------------------------------------------------

Report bugs
~~~~~~~~~~~

Please report bugs at https://github.com/renemarc/countdoom/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix bugs
~~~~~~~~

Look through the `GitHub issues`_ for bugs. Anything tagged with ``bug`` and
``help wanted`` is open to whoever wants to implement it.

Implement features
~~~~~~~~~~~~~~~~~~

Look through the `GitHub issues`_ for features. Anything tagged with
``enhancement`` and ``help wanted`` is open to whoever wants to implement it.

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


Get started! |badge-github| |badge-conventional-commits| |badge-codetriage|
---------------------------------------------------------------------------

.. |badge-github| image:: https://img.shields.io/badge/fork_me_on-GitHub-blue?logo=github&logoColor=white&cacheSeconds=86400
        :target: https://github.com/renemarc/countdoom
        :alt: GitHub

Ready to contribute? Here's how to set up |Countdoom| for local
development.

.. note::

    While |Countdoom| runs on Python 3.5+, many dev tools will require Python
    3.6+.

1. Fork the
   `Countdoom repo on GitHub <https://github.com/renemarc/countdoom/>`_.
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

  Alternatively, you can also use ``setup.py`` to install the above
  requirements:

  .. code-block:: console

        $ pip install --upgrade setuptools
        $ python setup.py develop

5. Create a branch for local development:

  .. code-block:: console

        $ git checkout -b name-of-your-bugfix-or-feature

  Now you can make your changes locally!

6. To help you test your code, you can use
`pyenv version manager <https://github.com/pyenv/pyenv>`_ to install
concurrent Python versions in local virtual environments (unless already
installed):

  .. code-block:: console

        $ pyenv install "3.5.9"
        $ pyenv install "3.6.10"
        $ pyenv install "3.7.6"
        $ pyenv install "3.8.1"
        $ pyenv install "pypy3.6-7.3.0"
        $ pyenv local "3.5.9" "3.6.10" "3.7.6" "3.8.1" "pypy3.6-7.3.0"

7. When you're done making changes, you can test the results with `makefile
<https://www.gnu.org/software/make/manual/make.html>`_. This will verify that
your changes pass this opinionated code quality gauntlet 🛡️:

  * `black <https://black.readthedocs.io/en/stable/>`_ code formatter
  * `flake8 <https://flake8.pycqa.org/>`_ style enforcer
  * `isort <https://isort.readthedocs.io/en/latest/>`_ imports checker
  * `mypy <http://mypy-lang.org/>`_ static type checker
  * `pylint <https://www.pylint.org/>`_ code analyzer
  * `pytest <https://docs.pytest.org/en/latest/>`_ python tests
  * `tox <https://tox.readthedocs.io/>`_ multi-version automated testing tool

  .. code-block:: console

        $ make test-all
        $ make coverage

  Alternatively, you can run the test suites individually:

  .. code-block:: console

        $ black --check --diff .
        $ flake8
        $ isort --check -rc .
        $ mypy
        $ pylint setup.py countdoom examples
        $ pylint --disable=E0401 tests/*.py
        $ pytest
        $ tox -e py35
        $ tox -e py36
        $ tox -e py37
        $ tox -e py38
        $ tox -e pypy3
        $ coverage

  .. note::

      To run a subset of tests, you can mention either the whole file or just
      one function:

      .. code-block:: console

          $ pytest tests/test_client.py
          $ pytest tests/test_client.py::test_valid_countdown

8. Commit your changes using `Conventional Commits`_ comment style and push your
branch to GitHub. To help catch any gotchas, `pre-commit
<https://pre-commit.com/>`_ will automatically run various code quality
linters on any modified files:

  .. code-block:: console

        $ git add .
        $ git commit -m "type(scope): detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

9. `Submit a pull request
<https://github.com/renemarc/countdoom/pulls>`_ through the GitHub website.


Pull request guidelines |badge-pulls|
-------------------------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, mention the change
   in the ``CHANGELOG.rst``, and if necessary add the feature to the list in
   ``README.md`` (repo) and ``README.rst`` (docs).
3. The pull request should work for Python 3.5, 3.6, 3.7, 3.8, and for PyPy3.
   Check https://travis-ci.com/renemarc/countdoom/pull_requests
   and make sure that the tests pass for all supported Python versions.


Deploying |badge-release| |badge-pypi| |badge-travis| |badge-docs|
------------------------------------------------------------------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in `CHANGELOG.rst
<https://github.com/renemarc/countdoom/blob/master/CHANGELOG.rst>`_).
Then run:

.. code-block:: console

    $ bumpversion patch # possible: major / minor / patch
    $ git push
    $ git push --tags

`Travis CI`_ will then deploy to the `Python Package Index`_ if tests pass.

.. |badge-codetriage| image:: https://www.codetriage.com/renemarc/countdoom/badges/users.svg
        :target: https://www.codetriage.com/renemarc/countdoom
        :alt: CodeTriage helpers

.. |badge-conduct| image:: https://img.shields.io/badge/code_of_conduct-Contributor_Covenant_v2.0-purple.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmIiBkPSJNMTIsMjEuMzVMMTAuNTUsMjAuMDNDNS40LDE1LjM2IDIsMTIuMjcgMiw4LjVDMiw1LjQxIDQuNDIsMyA3LjUsM0M5LjI0LDMgMTAuOTEsMy44MSAxMiw1LjA4QzEzLjA5LDMuODEgMTQuNzYsMyAxNi41LDNDMTkuNTgsMyAyMiw1LjQxIDIyLDguNUMyMiwxMi4yNyAxOC42LDE1LjM2IDEzLjQ1LDIwLjAzTDEyLDIxLjM1WiIgLz4KPC9zdmc+&cacheSeconds=86400
        :target: `Contributor Code of Conduct`_
        :alt: Contributor Convenant v2.0 Code of Conduct

.. |badge-contributors| image:: https://img.shields.io/badge/all_contributors-welcome-orange.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0xNiAxN1YxOUgyVjE3UzIgMTMgOSAxMyAxNiAxNyAxNiAxN00xMi41IDcuNUEzLjUgMy41IDAgMSAwIDkgMTFBMy41IDMuNSAwIDAgMCAxMi41IDcuNU0xNS45NCAxM0E1LjMyIDUuMzIgMCAwIDEgMTggMTdWMTlIMjJWMTdTMjIgMTMuMzcgMTUuOTQgMTNNMTUgNEEzLjM5IDMuMzkgMCAwIDAgMTMuMDcgNC41OUE1IDUgMCAwIDEgMTMuMDcgMTAuNDFBMy4zOSAzLjM5IDAgMCAwIDE1IDExQTMuNSAzLjUgMCAwIDAgMTUgNFoiIC8+Cjwvc3ZnPg==&cacheSeconds=86400
        :target: `all-contributors`_
        :alt: All Contributors

.. |badge-conventional-commits| image:: https://img.shields.io/badge/Conventional%20Commits-v1.0.0-yellow.svg?logo=git&logoColor=white&cacheSeconds=86400
        :target: `Conventional Commits`_
        :alt: Conventional Commits v1.0.0

.. |badge-docs| image:: https://img.shields.io/readthedocs/countdoom.svg?logo=read-the-docs&logoColor=White&cacheSeconds=21600
        :target: https://countdoom.readthedocs.io/en/latest/
        :alt: Documentation Status

.. |badge-issues| image:: https://img.shields.io/github/issues-raw/renemarc/countdoom?logo=github
        :target: `GitHub issues`_
        :alt: GitHub issues

.. |badge-license| image:: https://img.shields.io/github/license/renemarc/countdoom.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3LjgsMjBDMTcuNCwyMS4yIDE2LjMsMjIgMTUsMjJINUMzLjMsMjIgMiwyMC43IDIsMTlWMThINUwxNC4yLDE4QzE0LjYsMTkuMiAxNS43LDIwIDE3LDIwSDE3LjhNMTksMkMyMC43LDIgMjIsMy4zIDIyLDVWNkgyMFY1QzIwLDQuNCAxOS42LDQgMTksNEMxOC40LDQgMTgsNC40IDE4LDVWMThIMTdDMTYuNCwxOCAxNiwxNy42IDE2LDE3VjE2SDVWNUM1LDMuMyA2LjMsMiA4LDJIMTlNOCw2VjhIMTVWNkg4TTgsMTBWMTJIMTRWMTBIOFoiIGZpbGw9IiNmZmZmZmYiIC8+PC9zdmc+Cg==&cacheSeconds=86400
        :target: https://github.com/renemarc/countdoom/blob/master/LICENSE
        :alt: MIT license

.. |badge-pulls| image:: https://img.shields.io/github/issues-pr/renemarc/countdoom?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYsM0EzLDMgMCAwLDEgOSw2QzksNy4zMSA4LjE3LDguNDIgNyw4LjgzVjE1LjE3QzguMTcsMTUuNTggOSwxNi42OSA5LDE4QTMsMyAwIDAsMSA2LDIxQTMsMyAwIDAsMSAzLDE4QzMsMTYuNjkgMy44MywxNS41OCA1LDE1LjE3VjguODNDMy44Myw4LjQyIDMsNy4zMSAzLDZBMywzIDAgMCwxIDYsM002LDVBMSwxIDAgMCwwIDUsNkExLDEgMCAwLDAgNiw3QTEsMSAwIDAsMCA3LDZBMSwxIDAgMCwwIDYsNU02LDE3QTEsMSAwIDAsMCA1LDE4QTEsMSAwIDAsMCA2LDE5QTEsMSAwIDAsMCA3LDE4QTEsMSAwIDAsMCA2LDE3TTIxLDE4QTMsMyAwIDAsMSAxOCwyMUEzLDMgMCAwLDEgMTUsMThDMTUsMTYuNjkgMTUuODMsMTUuNTggMTcsMTUuMTdWN0gxNVYxMC4yNUwxMC43NSw2TDE1LDEuNzVWNUgxN0EyLDIgMCAwLDEgMTksN1YxNS4xN0MyMC4xNywxNS41OCAyMSwxNi42OSAyMSwxOE0xOCwxN0ExLDEgMCAwLDAgMTcsMThBMSwxIDAgMCwwIDE4LDE5QTEsMSAwIDAsMCAxOSwxOEExLDEgMCAwLDAgMTgsMTdaIiBmaWxsPSIjZmZmZmZmIiAvPjwvc3ZnPgo=&cacheSeconds=300
        :target: https://github.com/renemarc/countdoom/pulls
        :alt: GitHub issues

.. |badge-pypi| image:: https://img.shields.io/pypi/v/countdoom.svg?logo=pypi&logoColor=white&cacheSeconds=21600
        :target: `Python Package Index`_
        :alt: Python Package Index

.. |badge-release| image:: https://img.shields.io/github/release/renemarc/countdoom/all.svg?logo=git&logoColor=white&cacheSeconds=21600
        :target: https://github.com/renemarc/countdoom/releases/latest
        :alt: Latest release

.. |badge-travis| image:: https://img.shields.io/travis/com/renemarc/countdoom.svg?logo=travis-ci&logoColor=White
        :target: https://travis-ci.com/renemarc/countdoom
        :alt: Travis CI build status

.. _all-contributors: https://allcontributors.org/docs/en/specification
.. _Contributor Code of Conduct: https://github.com/renemarc/countdoom/blob/master/CODE_OF_CONDUCT.md
.. _Contributor Covenant: https://www.contributor-covenant.org/version/2/0/code_of_conduct/
.. _Conventional Commits: https://www.conventionalcommits.org/en/v1.0.0/
.. _GitHub issues: https://github.com/renemarc/countdoom/issues
.. _Python Package Index: https://pypi.org/project/countdoom/
.. _Travis CI: https://travis-ci.com/renemarc/countdoom

.. |Countdoom| replace:: **Countdoom**
