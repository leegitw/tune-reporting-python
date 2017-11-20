#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import pytest

from tune_reporting.tmc.v2.management.tmc_v2_advertisers import (
    TuneV2Advertisers
)
from requests_mv_integrations.exceptions import (
    TuneRequestBaseError
)
from tune_reporting.tmc.v2.management.tmc_v2_session_authenticate import (
    TuneV2AuthenticationTypes
)

@pytest.fixture
def tune_v2_advertisers_object():
    obj = TuneV2Advertisers()
    return obj

class TestTuneV2Advertisers:
    def test_tune_v2_advertisers_object(
        self,
        tmc_api_key,
        tune_v2_advertisers_object
    ):
        obj = tune_v2_advertisers_object
        try:
            obj.tmc_auth(tmc_api_key)
            assert(obj)

            if obj.get_advertiser_id(
                auth_value=tmc_api_key,
                auth_type=TuneV2AuthenticationTypes.API_KEY,
                request_retry=None
            ):
                assert(obj.advertiser_id)
            else:
                pytest.xfail("advertiser_id")

        except Exception as e:
            assert (isinstance(e, TuneRequestBaseError))
