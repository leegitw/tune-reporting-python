#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)

import sys
import logging
from pprintpp import pprint
from datetime import datetime, time, timedelta
import pytz

from tune_reporting.errors import (print_traceback, get_exception_message)
from tune_reporting.exceptions import (TuneReportingError)
from tune_reporting.tmc.v3.reporting import (TuneV3LogsAdvertisersImpressions, TuneV3LogsAdvertisersActions)
from tune_reporting.tmc.v2.management import (TuneV2AuthenticationTypes)
from logging_mv_integrations import (TuneLoggingFormat)


def main(tmc_api_key):

    tune_v3_logs_advertisers_impressions_find = \
        TuneV3LogsAdvertisersImpressions(
            logger_level=logging.DEBUG,
            logger_format=TuneLoggingFormat.JSON
        )

    tune_v3_logs_advertisers_impressions_find.logger_level = logging.DEBUG

    try:
        filter_stats_impressions = "(ad_network_id <> 0)"

        tz = pytz.timezone("America/New_York")
        yesterday = datetime.now(tz).date() - timedelta(days=1)
        str_yesterday = str(yesterday)

        tune_v3_logs_advertisers_impressions_find.collect(
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

    except TuneReportingError as tmv_ex:
        print(str(tmv_ex))

    except Exception as ex:
        print_traceback(ex)
        print(get_exception_message(ex))

    for row in list(tune_v3_logs_advertisers_impressions_find.generator):
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
