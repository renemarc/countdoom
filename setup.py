#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    README = readme_file.read()

with open('HISTORY.rst') as history_file:
    HISTORY = history_file.read()

REQUIREMENTS = [
    'aiohttp==3.6.2',
    'async-timeout==3.0.1',
    'beautifulsoup4==4.8.2',
    'Click==7.0',
]
REQUIREMENTS_SETUP = ['pytest-runner']
REQUIREMENTS_TEST = [
    'pytest',
    'pytest-asyncio',
    'pytest-httpserver',
    'requests',
]

setup(
    author="René-Marc Simard",
    author_email='renemarc@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Fetch the current Doomsday Clock from TheBulletin.org",
    entry_points={
        'console_scripts': ['doomsday_clock=doomsday_clock.cli:main']
    },
    install_requires=REQUIREMENTS,
    license="MIT license",
    long_description=README + '\n\n' + HISTORY,
    include_package_data=True,
    keywords='doomsday_clock',
    name='doomsday_clock',
    packages=find_packages(include=['doomsday_clock']),
    setup_requires=REQUIREMENTS_SETUP,
    test_suite='tests',
    tests_require=REQUIREMENTS_TEST,
    url='https://github.com/renemarc/doomsday_clock',
    version='0.1.0',
    zip_safe=False,
)
