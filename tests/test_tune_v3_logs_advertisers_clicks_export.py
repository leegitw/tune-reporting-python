#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)

import pytest
import logging
from datetime import datetime, timedelta
import pytz

from requests_mv_integrations.exceptions import (
    TuneRequestBaseError
)
from logging_mv_integrations import (
    LoggingFormat,
    LoggingOutput
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
    obj = TuneV3LogsAdvertisersClicks(
        logger_level=logging.INFO,
        logger_format=LoggingFormat.JSON,
        logger_output=LoggingOutput.STDOUT_COLOR
    )

    obj.logger_level = logging.DEBUG
    return obj


class TestTuneV3LogsAdvertisersClicksExport:
    def test_tune_v2_advertiser_clicks_export(
        self,
        tmc_api_key,
        tune_v3_logs_advertisers_clicks_object
    ):
        obj = tune_v3_logs_advertisers_clicks_object
        assert(obj)

        obj.logger_level = logging.DEBUG

        tz = pytz.timezone("America/New_York")
        yesterday = datetime.now(tz).date() - timedelta(days=1)
        str_yesterday = str(yesterday)

        try:
            obj.collect(
                auth_value=tmc_api_key,
                auth_type=TuneV2AuthenticationTypes.API_KEY,
                auth_type_use=TuneV2AuthenticationTypes.SESSION_TOKEN,
                start_date=str_yesterday,
                end_date=str_yesterday,
                advertiser_id=877,
                request_params={'timezone': 'America/New_York',
                                'filter': "(ad_network_id <> 0)",
                                'limit': 10},
                request_action=TuneV3LogsAdvertisersActions.EXPORT
            )
        except Exception as e:
            assert (isinstance(e, TuneRequestBaseError))

        for row in list(obj.generator):
            assert(row)
