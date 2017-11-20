#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import pytest
import logging
from requests_mv_integrations.exceptions import (
    TuneRequestBaseError
)
from tune_reporting.tmc.v2.management import (
    TuneV2AuthenticationTypes,
    TuneV2AdvertiserSites
)

@pytest.fixture
def tune_v2_advertiser_sites_object():
    obj = TuneV2AdvertiserSites(
        logger_level=logging.INFO
    )
    return obj

class TestTuneV2AdvertiserSites:
    def test_tune_v2_advertiser_sites(
        self,
        tmc_api_key,
        tune_v2_advertiser_sites_object
    ):
        obj = tune_v2_advertiser_sites_object
        try:
            obj.tmc_auth(tmc_api_key)
            assert(obj)

            obj.logger_level = logging.DEBUG

            for collect_data_item, collect_error in obj.collect(
                auth_value=tmc_api_key,
                auth_type=TuneV2AuthenticationTypes.API_KEY,
                auth_type_use=TuneV2AuthenticationTypes.API_KEY,
                request_params={'limit': 5}
            ):
                assert(collect_data_item)
                assert(collect_error is None)
                assert(len(collect_data_item) > 0)

        except Exception as e:
            assert (isinstance(e, TuneRequestBaseError))
