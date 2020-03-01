#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import sys
from typing import Dict, List

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    README = readme_file.read()

with open('HISTORY.rst') as history_file:
    HISTORY = history_file.read()

EXTRAS_REQUIRE = {
    'dist': [
        'bandit',
        'bump2version',
        'check-manifest',
        'flake8',
        'flake8-isort',
        'git-pylint-commit-hook',
        'pre-commit',
        'pylint',
        'pytoml',
        'setuptools',
        'twine',
        'wheel',
    ],
    'docs': [
        'argh',
        'm2r',
        'Sphinx',
        'sphinx-autodoc-typehints',
        'sphinx_rtd_theme',
        'watchdog',
    ],
    'lint': ['flake8', 'flake8-isort', 'isort', 'mypy', 'pylint', 'toml'],
    'test': [
        'aioresponses',
        'coverage',
        'pytest',
        'pytest-asyncio',
        'pytest-httpserver',
        'requests',
        'tox>=2.4',  # Support for `extras` command.
    ],
}  # type: Dict[str, List[str]]
if sys.version_info >= (3, 6):
    EXTRAS_REQUIRE['lint'] += ['black']
EXTRAS_REQUIRE['dev'] = sorted(
    {x for v in EXTRAS_REQUIRE.values() for x in v}, key=str.casefold
)

INSTALL_REQUIRES = [
    'aiohttp<4.0',  # >=4 is incompatible with Python 3.5.
    'beautifulsoup4',
]  # type: List[str]
if 'develop' in sys.argv:
    INSTALL_REQUIRES += EXTRAS_REQUIRE['dev']

SETUP_REQUIRES = []  # type: List[str]
if 'develop' in sys.argv:
    INSTALL_REQUIRES += [
        'pytest',
        # "setuptools",
        'tox',
        'twine',
        'wheel',
    ]
if 'test' in sys.argv:
    SETUP_REQUIRES += ["flake8", "flake8-import-order", "pytest-runner"]

TESTS_REQUIRE = [
    'aioresponses',
    'pytest',
    'pytest-asyncio',
    'pytest-httpserver',
    'requests',
]  # type: List[str]


setup(
    author="René-Marc Simard",
    author_email='renemarc@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description="Fetch the current Doomsday Clock from TheBulletin.org",
    entry_points={'console_scripts': ['countdoom=countdoom.cli:cli']},
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    keywords='Doomsday,Clock',
    license="MIT license",
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/x-rst",
    name='countdoom',
    packages=find_packages(include=['countdoom']),
    project_urls={
        'Documentation': 'https://countdoom.readthedocs.io/',
        # 'Changelog': '{}whatsnew-{}.html'.format(docs_url, branch_version),
        'Issue Tracker': 'https://github.com/renemarc/countdoom/issues',
    },
    python_requires='>=3.5',
    setup_requires=SETUP_REQUIRES,
    test_suite='tests',
    tests_require=TESTS_REQUIRE,
    url='https://github.com/renemarc/countdoom',
    version='0.1.0',
    zip_safe=False,
)
