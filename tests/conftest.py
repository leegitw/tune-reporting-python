#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
# content of conftest.py

def pytest_addoption(parser):
    parser.addoption("--tmc_api_key", action="append", default=[],
        help="list of tmc_api_key to pass to test functions")

def pytest_generate_tests(metafunc):
    if 'tmc_api_key' in metafunc.fixturenames:
        metafunc.parametrize("tmc_api_key",
                             metafunc.config.getoption('tmc_api_key'))