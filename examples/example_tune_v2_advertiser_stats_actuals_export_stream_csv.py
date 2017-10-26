#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import os
import sys
import csv
from pprintpp import pprint
from datetime import datetime, timedelta
import pytz
import logging

from requests_mv_integrations.exceptions import (TuneRequestBaseError)
from tune_reporting.errors import (print_traceback, get_exception_message)
from tune_reporting.exceptions import (TuneReportingError)
from tune_reporting.tmc.v2.reporting import (TuneV2AdvertiserStatsActuals, TuneV2AdvertiserStatsFormats)
from tune_reporting.support import (convert_size)
from tune_reporting.tmc.v2.management import (TuneV2AuthenticationTypes)
from logging_mv_integrations import (LoggingFormat)


def main(tmc_api_key):
    TIMEZONE_COLLECT = "America/New_York"

    export_format = TuneV2AdvertiserStatsFormats.CSV

    tune_v2_advertiser_stats_actuals = \
        TuneV2AdvertiserStatsActuals(
            timezone=TIMEZONE_COLLECT,
            logger_level=logging.INFO,
            logger_format=LoggingFormat.JSON
        )

    dw_file_path = "data.{}".format(export_format)
    if os.path.exists(dw_file_path):
        os.remove(dw_file_path)

    tz = pytz.timezone(TIMEZONE_COLLECT)
    yesterday = datetime.now(tz).date() - timedelta(days=1)
    str_yesterday = str(yesterday)

    try:
        tune_v2_advertiser_stats_actuals.tmc_auth(tmc_api_key=tmc_api_key)

        response = tune_v2_advertiser_stats_actuals.stream(
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
                print(row)

        statinfo = os.stat(dw_file_path)
        extra = {
            'response_status_code': response.status_code,
            'response_headers': response.headers,
            'dw_file_path': dw_file_path,
            'dw_file_size': convert_size(statinfo.st_size)
        }

        pprint(extra)

    except TuneRequestBaseError as tmc_req_ex:
        print_traceback(tmc_req_ex)
        pprint(tmc_req_ex.to_dict())
        print(str(tmc_req_ex))

    except TuneReportingError as tmc_rep_ex:
        pprint(tmc_rep_ex.to_dict())
        print(str(tmc_rep_ex))

    except Exception as ex:
        print_traceback(ex)
        print(get_exception_message(ex))


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError("{} [tmc_api_key].".format(sys.argv[0]))
        tmc_api_key = sys.argv[1]
        sys.exit(main(tmc_api_key))
    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise
