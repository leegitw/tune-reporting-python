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
from logging_mv_integrations import (
    LoggingFormat,
    LoggingOutput
)
from tune_reporting.tmc.v2.reporting import (
    TuneV2AdvertiserStatsActuals,
    TuneV2AdvertiserStatsActions,
    TuneV2AdvertiserStatsFormats
)
from tune_reporting.tmc.v2.management import (
    TuneV2AuthenticationTypes
)

@pytest.fixture
def tune_v2_advertiser_stats_actuals_object():
    obj = TuneV2AdvertiserStatsActuals(
        logger_level=logging.INFO,
        logger_format=LoggingFormat.JSON,
        logger_output=LoggingOutput.STDOUT_COLOR
    )
    return obj

class TestTuneV2AdvertiserStatsActualsExportDownload:
    def test_tune_v2_advertiser_stats_actuals_export_download(
        self,
        tmc_api_key,
        tune_v2_advertiser_stats_actuals_object
    ):
        assert(tmc_api_key)
        assert(len(tmc_api_key) > 1)

        obj = tune_v2_advertiser_stats_actuals_object
        assert(obj)

        obj.logger_level = logging.DEBUG

        tz = pytz.timezone("America/New_York")
        yesterday = datetime.now(tz).date() - timedelta(days=1)
        str_yesterday = str(yesterday)

        try:
            obj.tmc_auth(tmc_api_key)

            obj.collect(
                auth_value=tmc_api_key,
                auth_type=TuneV2AuthenticationTypes.API_KEY,
                auth_type_use=TuneV2AuthenticationTypes.API_KEY,
                start_date=str_yesterday,
                end_date=str_yesterday,
                request_params={
                    'timezone': 'America/Los_Angeles',
                    'format': TuneV2AdvertiserStatsFormats.CSV,
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
                    'timezone': "America/Los_Angeles",
                    'limit': 5
                },
                request_action=TuneV2AdvertiserStatsActions.EXPORT,
                request_retry={'delay': 15,
                               'timeout': 30,
                               'tries': 10}
            )
        except Exception as e:
            assert (isinstance(e, TuneRequestBaseError))

        for row in list(obj.generator):
            assert(row)