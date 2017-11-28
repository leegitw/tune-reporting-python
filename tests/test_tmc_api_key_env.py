#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import os

class TestTmcApiKey:
    def test_env(
        self,
        tmc_api_key
    ):
        assert(tmc_api_key is not None)
        assert(len(tmc_api_key) > 1)

        env_home = os.environ.get('HOME')
        assert(env_home is not None)

        env_tmc_api_key = os.environ.get('TMC_API_KEY')
        assert(env_tmc_api_key is not None)
        assert(env_tmc_api_key == tmc_api_key)

    def test_config(
        self,
        tmc_api_key
    ):
        assert(tmc_api_key is not None)
        assert(len(tmc_api_key) > 1)