#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import pytest
import logging

from tune_reporting.tmc.v2.management import (TuneV2SessionAuthenticate)
from requests_mv_integrations.exceptions import (TuneRequestBaseError)

@pytest.fixture
def tune_v2_session_authenticate():
    obj = TuneV2SessionAuthenticate(
        logger_level=logging.INFO
    )
    return obj

class TestTuneV2SessionAuthenticate:
    def test_tune_v2_session_authenticate(
        self,
        tmc_api_key,
        tune_v2_session_authenticate
    ):
        obj = tune_v2_session_authenticate
        assert(obj)

        try:
            if obj.get_session_token(
                    tmc_api_key=tmc_api_key,
                    request_retry=None
            ):
                session_token = tune_v2_session_authenticate.session_token
                assert(session_token)
            else:
                pytest.xfail("session_authenticate")
        except Exception as e:
            assert(isinstance(e, TuneRequestBaseError))
