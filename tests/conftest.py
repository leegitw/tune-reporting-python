#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)
# content of conftest.py

import pytest
import os

@pytest.fixture
def tmc_api_key():
    return os.environ.get('TMC_API_KEY')

