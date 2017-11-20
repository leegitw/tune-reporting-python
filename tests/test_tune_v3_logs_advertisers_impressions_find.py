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
    TuneV3LogsAdvertisersImpressions,
    TuneV3LogsAdvertisersActions
)
from tune_reporting.tmc.v2.management import (TuneV2AuthenticationTypes)
from logging_mv_integrations import (LoggingFormat, LoggingOutput)

@pytest.fixture
def tune_v3_logs_advertisers_impressions_object():
    obj = TuneV3LogsAdvertisersImpressions(
        logger_level=logging.INFO,
        logger_format=LoggingFormat.JSON,
        logger_output=LoggingOutput.STDOUT_COLOR
    )
    return obj

class TestTuneV3LogsAdvertisersImpressionsFind:
    def test_tune_v2_advertiser_impressions_find(
        self,
        tmc_api_key,
        tune_v3_logs_advertisers_impressions_object
    ):
        obj = tune_v3_logs_advertisers_impressions_object
        assert(obj)

        obj.logger_level = logging.DEBUG

        try:
            filter_stats_impressions = "(ad_network_id <> 0)"

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
                                'filter': filter_stats_impressions,
                                'limit': 5},
                request_action=TuneV3LogsAdvertisersActions.FIND
            )
        except Exception as e:
            assert (isinstance(e, TuneRequestBaseError))

        # for row in list(obj.generator):
        #     assert(row)
