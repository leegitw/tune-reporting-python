#   Makefile
#
#   Copyright (c) 2016 Tune, Inc
#   All rights reserved.
#

.PHONY: clean venv install analysis examples27 examples3 tests tests-travis-ci tests-install build27 build3 dist dist27 dist3 register27 register3 docs-sphinx docs-doxygen

PYTHON3 := $(shell which python3)
PIP3    := $(shell which pip3)

TUNE_REPORTING_PKG := tune-reporting
TUNE_REPORTING_PKG_PREFIX := tune_reporting

TUNE_PKG_SUFFIX := py3-none-any.whl
TUNE_REPORTING_PKG_WILDCARD := $(TUNE_REPORTING_PKG)-*
TUNE_REPORTING_PKG_PREFIX_WILDCARD := $(TUNE_REPORTING_PKG_PREFIX)-*
TUNE_REPORTING_PKG_PATTERN := $(TUNE_REPORTING_PKG_PREFIX)-*-$(TUNE_PKG_SUFFIX)

VERSION := $(shell $(PYTHON3) setup.py version)
TUNE_REPORTING_WHEEL_ARCHIVE := dist/$(TUNE_REPORTING_PKG_PREFIX)-$(VERSION)-$(TUNE_PKG_SUFFIX)

TUNE_REPORTING_FILES := $(shell find $(TUNE_REPORTING_PKG_PREFIX) ! -name '__init__.py' -type f -name "*.py")
LINT_REQ_FILE := requirements-pylint.txt
REQ_FILE      := requirements.txt
SETUP_FILE    := setup.py
ALL_FILES     := $(TUNE_REPORTING_FILES) $(REQ_FILE) $(SETUP_FILE)


# Report the current tune-reporting version.
version:
	@echo TUNE Reporting SDK Base Version: $(VERSION)


# Upgrade pip. Note that this does not install pip if you don't have it.
# Pip must already be installed to work with this Makefile.
pip-upgrade:
	$(PIP3) install --upgrade pip

install:
	$(PIP3) install --upgrade -r requirements.txt

tests-install: install
	. venv/bin/activate; pip install --upgrade -r tests/requirements.txt

clean:
	@echo "======================================================"
	@echo clean
	@echo "======================================================"
	rm -fR __pycache__ venv "*.pyc" build/*    \
		$(TUNE_REPORTING_PKG_PREFIX)/__pycache__/         \
		$(TUNE_REPORTING_PKG_PREFIX)/helpers/__pycache__/ \
		$(TUNE_REPORTING_PKG_PREFIX).egg-info/*
	find ./* -maxdepth 0 -name "*.pyc" -type f -delete
	find $(TUNE_REPORTING_PKG_PREFIX) -name "*.pyc" -type f -delete

# Install the project requirements.
requirements: pip-upgrade
	$(PIP3) install --upgrade -r $(REQ_FILE)

build: $(ALL_FILES) requirements
	@echo "======================================================"
	@echo build: $(TUNE_REPORTING_PKG)
	@echo "======================================================"
	$(PYTHON3) $(SETUP_FILE) clean
	$(PYTHON3) $(SETUP_FILE) build
	$(PYTHON3) $(SETUP_FILE) install

uninstall-package: clean
	@echo "======================================================"
	@echo uninstall-package: $(TUNE_REPORTING_PKG)
	@echo "======================================================"
	$(PIP3) install --upgrade list
	@if $(PIP3) list --format=legacy | grep -F $(TUNE_REPORTING_PKG) > /dev/null; then \
		echo "python package $(TUNE_REPORTING_PKG) Found"; \
		$(PIP3) uninstall --yes $(TUNE_REPORTING_PKG); \
	else \
		echo "python package $(TUNE_REPORTING_PKG) Not Found"; \
	fi;

# Install the module from a binary distribution archive.
install: remove-package
	@echo "======================================================"
	@echo install: $(TUNE_REPORTING_PKG)
	@echo "======================================================"
	@echo Installing: $(TUNE_REPORTING_PKG)
	$(PIP3) install --upgrade pip
	$(PIP3) install --upgrade $(TUNE_REPORTING_WHEEL_ARCHIVE)
	$(PIP3) freeze | grep $(TUNE_REPORTING_PKG)

freeze:
	@echo "======================================================"
	@echo freeze: $(TUNE_REPORTING_PKG)
	@echo "======================================================"
	$(PIP3) install --upgrade freeze
	$(PIP3) freeze | grep $(TUNE_REPORTING_PKG)

dist-install:
	$(PIP3) install -r requirements.txt

dist:
	rm -fR ./dist/*
	$(PYTHON3) setup.py sdist --format=zip,gztar upload
	$(PYTHON3) setup.py bdist_egg upload
	$(PYTHON3) setup.py bdist_wheel upload

register:
	$(PYTHON3) setup.py register

tests: build
	$(PYTHON3) ./tests/tune_reporting_tests.py $(api_key)

tests-travis-ci:
	flake8 --ignore=F401,E265,E129 tune
	flake8 --ignore=E123,E126,E128,E265,E501 tests
	$(PYTHON3) ./tests/tune_reporting_tests.py $(api_key)

site-packages:
	@echo "======================================================"
	@echo site-packages: $(TUNE_REPORTING_PKG)
	@echo "======================================================"
	@echo $(PYTHON3_SITE_PACKAGES)

list-package:
	@echo "======================================================"
	@echo list-package: $(TUNE_REPORTING_PKG)
	@echo "======================================================"
	ls -al $(PYTHON3_SITE_PACKAGES)/$(TUNE_REPORTING_PKG_PREFIX)*

remove-package: uninstall-package
	@echo "======================================================"
	@echo remove-package: $(TUNE_REPORTING_PKG)
	@echo "======================================================"
	rm -fR $(PYTHON3_SITE_PACKAGES)/$(TUNE_REPORTING_PKG_PREFIX)*

local-dev: remove-package
	@echo "======================================================"
	@echo local-dev: $(TUNE_REPORTING_PKG)
	@echo "======================================================"
	$(PIP3) install --upgrade freeze
	$(PIP3) install --upgrade .
	$(PIP3) freeze | grep $(TUNE_REPORTING_PKG)

lint: clean
	pylint --rcfile ./tools/pylintrc tune_reporting | more

lint-requirements: $(LINT_REQ_FILE)
	$(PIP3) install --upgrade -f $(LINT_REQ_FILE)

pep8: lint-requirements
	@echo pep8: $(TUNE_REPORTING_FILES)
	$(PYTHON3) -m pep8 --config .pep8 $(TUNE_REPORTING_FILES)

pyflakes: lint-requirements
	@echo pyflakes: $(TUNE_REPORTING_FILES)
	$(PYTHON3) -m pyflakes $(TUNE_REPORTING_FILES)

pylint: lint-requirements
	@echo pylint: $(TUNE_REPORTING_FILES)
	$(PIP3) install --upgrade pylint
	$(PYTHON3) -m pylint --rcfile .pylintrc $(TUNE_REPORTING_FILES) --disable=C0330,F0401,E0611,E0602,R0903,C0103,E1121,R0913,R0902,R0914,R0912,W1202,R0915,C0302 | more -30

docs-sphinx-gen:
	rm -fR ./docs/sphinx/tune_reporting/*
	sphinx-apidoc -o ./docs/sphinx/tune_reporting/ ./tune_reporting

docs-install: venv
	. venv/bin/activate; pip install -r docs/sphinx/requirements.txt

docs-sphinx: docs-install
	rm -fR ./docs/sphinx/_build
	cd docs/sphinx && make html
	x-www-browser docs/sphinx/_build/html/index.html

docs-doxygen:
	rm -fR ./docs/doxygen/*
	sudo doxygen docs/Doxyfile
	x-www-browser docs/doxygen/html/index.html
