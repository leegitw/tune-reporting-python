#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import os
import pytest
import logging
import pytz
import csv
from datetime import datetime, timedelta
from requests_mv_integrations.exceptions import (
    TuneRequestBaseError
)
from logging_mv_integrations import (
    LoggingFormat,
    LoggingOutput
)
from tune_reporting.tmc.v2.management import (
    TuneV2AuthenticationTypes
)
from tune_reporting.tmc.v2.reporting import (
    TuneV2AdvertiserStatsActuals,
    TuneV2AdvertiserStatsFormats
)

TIMEZONE_COLLECT = "America/New_York"

@pytest.fixture
def tune_v2_advertiser_stats_actuals_object():

    obj = TuneV2AdvertiserStatsActuals(
        timezone=TIMEZONE_COLLECT,
        logger_level=logging.INFO,
        logger_format=LoggingFormat.JSON,
        logger_output=LoggingOutput.STDOUT_COLOR
    )
    return obj

class TestTuneV2AdvertiserStatsActualsExportStreamCsv:
    def test_tune_v2_advertiser_stats_actuals_export_stream_csv(
        self,
        tmc_api_key,
        tune_v2_advertiser_stats_actuals_object
    ):
        obj = tune_v2_advertiser_stats_actuals_object
        assert(obj)

        obj.logger_level = logging.DEBUG

        export_format = TuneV2AdvertiserStatsFormats.CSV

        dw_file_path = "data.{}".format(export_format)
        if os.path.exists(dw_file_path):
            os.remove(dw_file_path)

        tz = pytz.timezone(TIMEZONE_COLLECT)
        yesterday = datetime.now(tz).date() - timedelta(days=1)
        str_yesterday = str(yesterday)

        try:
            obj.tmc_auth(tmc_api_key)

            response = obj.stream(
                auth_value=tmc_api_key,
                auth_type=TuneV2AuthenticationTypes.API_KEY,
                auth_type_use=TuneV2AuthenticationTypes.API_KEY,
                start_date=str_yesterday,
                end_date=str_yesterday,
                request_params={
                    'format': export_format,
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
                    'timezone': "America/Los_Angeles"
                },
                request_retry={'delay': 15,
                               'timeout': 30,
                               'tries': 10}
            )

            with open(file=dw_file_path, mode='wb') as dw_file_wb:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        dw_file_wb.write(chunk)
                dw_file_wb.flush()

            with open(file=dw_file_path, mode='r') as csv_file_r:
                csv_dict_reader = csv.DictReader(csv_file_r)
                for row in csv_dict_reader:
                    assert(row)

            assert(dw_file_path)
            statinfo = os.stat(dw_file_path)
            assert(statinfo)
            assert(response.status_code == 200)
        except Exception as e:
            assert (isinstance(e, TuneRequestBaseError))
