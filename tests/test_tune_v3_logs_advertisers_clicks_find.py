#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import pytest
import logging
from datetime import datetime, timedelta
import pytz
from requests_mv_integrations.exceptions import (
    TuneRequestBaseError
)
from tune_reporting.tmc.v3.reporting import (
    TuneV3LogsAdvertisersClicks,
    TuneV3LogsAdvertisersActions
)
from tune_reporting.tmc.v2.management import (
    TuneV2AuthenticationTypes
)

@pytest.fixture
def tune_v3_logs_advertisers_clicks_object():
    obj = TuneV3LogsAdvertisersClicks()
    return obj

class TestTuneV3LogsAdvertisersClicksFind:
    def test_tune_v2_advertiser_clicks_find(
        self,
        tmc_api_key,
        tune_v3_logs_advertisers_clicks_object
    ):
        obj = tune_v3_logs_advertisers_clicks_object
        assert(obj)

        obj.logger_level = logging.DEBUG

        filter_stats_clicks = "(ad_network_id <> 0)"

        tz = pytz.timezone("America/New_York")
        yesterday = datetime.now(tz).date() - timedelta(days=1)
        str_yesterday = str(yesterday)

        obj.collect(
            auth_value=tmc_api_key,
            auth_type=TuneV2AuthenticationTypes.API_KEY,
            auth_type_use=TuneV2AuthenticationTypes.SESSION_TOKEN,
            start_date=str_yesterday,
            end_date=str_yesterday,
            advertiser_id=877,
            request_params={'timezone': 'America/New_York',
                            'filter': filter_stats_clicks,
                            'limit': 10},
            request_action=TuneV3LogsAdvertisersActions.FIND
        )

        for row in list(obj.generator):
            assert(row)

        try:
            obj.tmc_auth(tmc_api_key)
        except Exception as e:
            assert (isinstance(e, TuneRequestBaseError))
