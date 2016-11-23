#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)

import sys
from pprintpp import pprint
from datetime import datetime, timedelta
import pytz
import logging

from tune_reporting.errors import (print_traceback, get_exception_message)
from tune_reporting.errors import (TuneReportingError)
from tune_reporting.tmc.v2.reporting import (
    TuneV2AdvertiserStatsActuals, TuneV2AdvertiserStatsActions, TuneV2AdvertiserStatsFormats
)
from tune_reporting.tmc.v2.management import (TuneV2AuthenticationTypes)
from logging_mv_integrations import (TuneLoggingFormat)


def main(tmc_api_key):

    tune_v2_advertiser_stats_actuals = \
        TuneV2AdvertiserStatsActuals(
            logger_level=logging.DEBUG,
            logger_format=TuneLoggingFormat.JSON
        )

    tz = pytz.timezone("America/New_York")
    yesterday = datetime.now(tz).date() - timedelta(days=1)
    str_yesterday = str(yesterday)

    try:
        auth_response = tune_v2_advertiser_stats_actuals.tmc_auth(tmc_api_key=tmc_api_key)

        tune_v2_advertiser_stats_actuals.collect(
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

    except TuneReportingError as tmv_ex:
        print(str(tmv_ex))

    except Exception as ex:
        print_traceback(ex)
        print(get_exception_message(ex))

    for row in list(tune_v2_advertiser_stats_actuals.generator):
        pprint(row)


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError("{} [tmc_api_key].".format(sys.argv[0]))
        tmc_api_key = sys.argv[1]
        sys.exit(main(tmc_api_key))
    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise
