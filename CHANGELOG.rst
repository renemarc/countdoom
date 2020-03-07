******************************************
Changelog |badge-changelog| |badge-semver|
******************************************

All notable changes to **Countdoom** will be documented in this list. The
format is based on `Keep a Changelog`_, and this project adheres to
`Semantic Versioning`_.

`Unreleased`_ |badge-commits-since-release|
===========================================

*No documented unreleased changes*


`v0.2.1`_ — 2020-03-07
======================

Added
-----

- `Code of Conduct`_ based on `Contributor Covenant`_.
- Continuous deployment to PyPI when new versions are pushed to the repo.

Fixed
-----

- Spelling, links and images in documentation.

.. _Code of Conduct: https://github.com/renemarc/countdoom/blob/master/CODE_OF_CONDUCT.md
.. _Contributor Covenant: https://www.contributor-covenant.org/version/2/0/code_of_conduct/

`v0.2.0`_ — 2020-03-03
======================

Alpha release. Since the `Doomsday Clock
<https://thebulletin.org/doomsday-clock/>`__ has (…unfortunately 😩) started
counting in seconds for the first time since 1947, the code was adapted to also
handle sub-minute values.

Added
-----

- ``minutes`` as an output format option and in returned data set.
- Repo-specific `Markdown README file`_.
- Documentation at `Read The Docs`_.
- Pull Request template.
- Support for `All Contributors`_ specifications and service app.
- Support for `Code Climate`_ code quality checker service.
- Support for `CodeCov`_ test coverage report analyzer service.
- Support for `DeepSource`_ code security checker service.
- Support for `Keep a Changelog`_ specifications.
- Support for `mypy`_ static type checker.
- Support for `Probot's Auto-Comment`_ response service app.
- Support for `Probot's helPR`_ issue labeler service app.
- Support for `Probot's No Response Info`_ issue closing service app.
- Support for `Probot's Request Info`_ issue validating service app.
- Support for `Probot's Stale Info`_ auto-closing service app.
- Support for `Probot's Welcome`_ greeting service app.

Changed
-------

- **BREAKING:** Return countdown in seconds instead of minutes.
- **BREAKING:** Rename project to **Countdoom**.
- Expand Tox test environments to include Python 3.5–3.8, Pypy3, formatter,
  and linters.
- Expand test coverage to cover seconds to midnight.
- Improve type hints.
- Expand contributing guidelines.
- Improve install documentation.
- Move Asyncio loop handling from package ``__main__.py`` to ``cli.py``.
- Simplify support tools configuration files.
- Regroup dependencies listing to ``setup.py``.
- Add descriptive file headers and modelines.
- Split `Issue template`_ into *Bug Report*, *Feature Request*, *Questions and
  Help*, and *Agile User Story*.

Fixed
-----

- Revise sentence extraction logic to include seconds to midnight.

Removed
-------

- Files ``requirements.txt`` and ``requirements_dev.txt`` (now in ``setup.py``).
- Support for `Pyup`_ dependency checker service.


.. _Markdown README file: https://github.com/renemarc/countdoom
.. _Read The Docs: https://countdoom.readthedocs.io/
.. _All Contributors: https://allcontributors.org/
.. _Code Climate: https://codeclimate.com/github/renemarc/countdoom
.. _CodeCov: https://codecov.io/gh/renemarc/countdoom
.. _DeepSource: https://deepsource.io/gh/renemarc/countdoom/
.. _mypy: http://mypy-lang.org
.. _Probot's Auto-Comment: https://probot.github.io/apps/auto-comment/
.. _Probot's helPR: https://probot.github.io/apps/helpr/
.. _Probot's No Response Info: https://probot.github.io/apps/no-response/
.. _Probot's Request Info: https://probot.github.io/apps/request-info/
.. _Probot's Stale Info: https://probot.github.io/apps/stale/
.. _Probot's Welcome: https://probot.github.io/apps/welcome/
.. _Issue template: https://github.com/renemarc/countdoom/issues/new/choose

`v0.1.0`_ — 2020-02-23
======================

Inital release.

Added
-----

- Extraction of minutes to midnight from `TheBulletin.org`_.
- Tests with `pytest`_.
- Command-line interface.
- Integration examples.
- Importable client module with `Asyncio`_ support.
- `Makefile`_ build assistant.
- Basic `Sphinx`_ documentation.
- `Badges`_ to README file.
- Support for `bandit`_ security issues checker.
- Support for `Black`_ code formatter.
- Support for `Coverage.py`_ unit tests measuring tool.
- Support for `EditorConfig`_ coding style config file.
- Support for `Flake8`_ coding style enforcer.
- Support for `isort`_ imports organizer.
- Support for `pip`_ dependencies manager.
- Support for `pre-commit`_ git hooks with linters, formatters, and validators.
- Support for `Pylint`_ code analyzer.
- Support for `Pyup`_ dependency checker service.
- Support for `Tox`_ automation integration.
- Support for `Travis-CI`_ continuous integration service.


.. _Asyncio: https://docs.python.org/3/library/asyncio.html
.. _Badges: https://shields.io/
.. _bandit: https://bandit.readthedocs.io/
.. _Black: https://black.readthedocs.io/
.. _Coverage.py: https://coverage.readthedocs.io/
.. _EditorConfig: https://editorconfig.org/
.. _Flake8: https://flake8.pycqa.org/
.. _isort: https://github.com/timothycrosley/isort
.. _Keep a Changelog: https://keepachangelog.com/en/1.0.0/
.. _Makefile: https://www.gnu.org/software/make/manual/make.html
.. _pip: https://pip.pypa.io/
.. _pre-commit: https://pre-commit.com/
.. _Pylint: https://www.pylint.org/
.. _pytest: https://docs.pytest.org/
.. _Pyup: https://pyup.io/
.. _Semantic Versioning: https://semver.org/spec/v2.0.0.html
.. _Sphinx: https://www.sphinx-doc.org/
.. _TheBulletin.org: https://thebulletin.org
.. _Tox: https://tox.readthedocs.io/
.. _Travis-CI: https://travis-ci.com/renemarc/countdoom


.. _Unreleased: https://github.com/renemarc/countdoom/compare/v0.2.1...master
.. _v0.2.1: https://github.com/renemarc/countdoom/releases/tag/v0.2.1
.. _v0.2.0: https://github.com/renemarc/countdoom/releases/tag/v0.2.0
.. _v0.1.0: https://github.com/renemarc/countdoom/releases/tag/v0.1.0


.. |badge-changelog| image:: https://img.shields.io/badge/keep%20a%20changelog-v1.0.0-%23E05735?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik01LDE1LjVMNy41LDIwSDIuNUw1LDE1LjVNOSwxOUgyMVYxN0g5VjE5TTUsOS41TDcuNSwxNEgyLjVMNSw5LjVNOSwxM0gyMVYxMUg5VjEzTTUsMy41TDcuNSw4SDIuNUw1LDMuNU05LDdIMjFWNUg5VjdaIiAvPgo8L3N2Zz4=&cacheSeconds=86400
        :target: `Keep a Changelog`_
        :alt: Keep a Changelog v1.0.0

.. |badge-commits-since-release| image:: https://img.shields.io/github/commits-since/renemarc/countdoom/latest.svg?label=commits%20to%20be%20deployed&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KCTxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0xMy41LDhIMTJWMTNMMTYuMjgsMTUuNTRMMTcsMTQuMzNMMTMuNSwxMi4yNVY4TTEzLDNBOSw5IDAgMCwwIDQsMTJIMUw0Ljk2LDE2LjAzTDksMTJINkE3LDcgMCAwLDEgMTMsNUE3LDcgMCAwLDEgMjAsMTJBNyw3IDAgMCwxIDEzLDE5QzExLjA3LDE5IDkuMzIsMTguMjEgOC4wNiwxNi45NEw2LjY0LDE4LjM2QzguMjcsMjAgMTAuNSwyMSAxMywyMUE5LDkgMCAwLDAgMjIsMTJBOSw5IDAgMCwwIDEzLDMiIC8+Cjwvc3ZnPgo=&cacheSeconds=300
        :target: `Unreleased`_
        :alt: Commits to be deployed

.. |badge-semver| image:: https://img.shields.io/badge/semver-v2.0.0-black?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0xNC42LDE2LjZMMTkuMiwxMkwxNC42LDcuNEwxNiw2TDIyLDEyTDE2LDE4TDE0LjYsMTYuNk05LjQsMTYuNkw0LjgsMTJMOS40LDcuNEw4LDZMMiwxMkw4LDE4TDkuNCwxNi42WiIgLz4KPC9zdmc+&cacheSeconds=86400
        :target: `Semantic Versioning`_
        :alt: Semantic Versioning v2.0.0
