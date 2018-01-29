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
from tune_reporting.tmc.v2.management import (
    TuneV2AuthenticationTypes
)
from logging_mv_integrations import (
    LoggingFormat,
    LoggingOutput
)
from tune_reporting.tmc.v2.reporting import (
    TuneV2AdvertiserStatsActuals,
    TuneV2AdvertiserStatsActions
)


@pytest.fixture
def tune_v2_advertiser_stats_actuals_object():
    obj = \
        TuneV2AdvertiserStatsActuals(
            logger_level=logging.INFO,
            logger_format=LoggingFormat.JSON,
            logger_output=LoggingOutput.STDOUT_COLOR
        )
    return obj


class TestTuneV2AdvertiserStatsActualsFind:
    def test_tune_v2_advertiser_sites_object(
        self,
        tmc_api_key,
        tune_v2_advertiser_stats_actuals_object
    ):
        obj = tune_v2_advertiser_stats_actuals_object
        assert(obj)

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
                request_params={
                    'fields': (
                        "ad_clicks,"
                        "ad_clicks_unique,"
                        "ad_impressions,"
                        "ad_impressions_unique,"
                        "ad_network_id,"
                        "advertiser_id,"
                        "country.code,"
                        "date_hour,"
                        "events,"
                        "installs,"
                        "is_reengagement,"
                        "payouts,"
                        "publisher_id,"
                        "publisher_sub_ad.ref,"
                        "publisher_sub_adgroup.ref,"
                        "publisher_sub_campaign.ref,"
                        "publisher_sub_publisher.ref,"
                        "publisher_sub_site.ref,"
                        "site_id"
                    ),
                    'group': (
                        "country_id,"
                        "is_reengagement,"
                        "publisher_id,"
                        "publisher_sub_ad_id,"
                        "publisher_sub_adgroup_id,"
                        "publisher_sub_campaign_id,"
                        "publisher_sub_publisher_id,"
                        "publisher_sub_site_id,"
                        "site_id"
                    ),
                    'timezone': 'America/New_York',
                    'limit': 5
                },
                request_action=TuneV2AdvertiserStatsActions.FIND
            )

        except Exception as e:
            assert (isinstance(e, TuneRequestBaseError))

        for row in list(obj.generator):
            assert(row)
