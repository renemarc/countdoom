# -*-mode:makefile-*- vim:ft=makefile

# Build assistant using make
#
# Contains a set of directives used by the make build automation tool to
# generate targets/goals.
# Type `make` to see usage information.
# See https://www.gnu.org/software/make/manual/make.html

.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("  %-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@printf "\n"
	@printf " 11 12   \n"
	@printf "10 \|    \e[0;1mCountdoom\e[0m\n"
	@printf "9   @    \e[0;1mMakefile\e[0m\n"
	@printf "\n"
	@printf "\e[4mUsage\e[0m\n"
	@printf "  make [target...]\n"
	@printf "\n"
	@printf "\e[4mAvailable targets\e[0m\n"
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)
	@printf "\n"

clean: clean-build clean-docs clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-docs: ## remove Sphynx documentation
	rm -fr docs/_build/

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .mypy_cache/
	rm -fr .pytest_cache

lint: ## check style with flake8,mypy, and pylint
	flake8
	mypy
	pylint ./**/*.py

secure: ## check code for security issues
	bandit --recursive countdoom docs

test: ## run tests quickly with the default Python
	pytest

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source countdoom --module pytest;
	coverage report --show-missing
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	sphinx-apidoc --force --output-dir docs/ countdoom
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

docs-builder: ## build Sphinx HTML documentation
	sphinx-build -b html docs/ docs/_build/
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	pip install --upgrade twine
	twine check dist/*
	twine upload dist/*

test-release: dist ## package and upload a release to TestPyPI
	pip install --upgrade twine
	twine check dist/*
	twine upload --verbose --repository-url https://test.pypi.org/legacy/ dist/*

dist: clean ## build source and wheel package
	pip install --upgrade setuptools wheel
	pip install --upgrade twine
	python setup.py sdist
	python setup.py bdist_wheel
	twine check dist/*
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

uninstall: _uninstall clean ## uninstall the package from the active Python's site-packages

_uninstall:
	pip uninstall -y countdoom
