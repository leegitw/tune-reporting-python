#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)

import sys
import logging
from pprintpp import pprint
from datetime import datetime, timedelta
import pytz

from requests_mv_integrations.exceptions import (TuneRequestBaseError)
from tune_reporting.errors import (print_traceback, get_exception_message)
from tune_reporting.exceptions import (TuneReportingError)
from tune_reporting.tmc.v3.reporting import (
    TuneV3LogsAdvertisersClicks,
    TuneV3LogsAdvertisersActions
)
from tune_reporting.tmc.v2.management import (
    TuneV2AuthenticationTypes
)
from logging_mv_integrations import (
    LoggingFormat,
    LoggingOutput
)


def main(tmc_api_key):
    tune_v3_logs_advertisers_clicks_export = \
        TuneV3LogsAdvertisersClicks(
            logger_level=logging.INFO,
            logger_format=LoggingFormat.JSON,
            logger_output=LoggingOutput.STDOUT_COLOR
        )

    tune_v3_logs_advertisers_clicks_export.logger_level = logging.DEBUG

    tz = pytz.timezone("America/New_York")
    yesterday = datetime.now(tz).date() - timedelta(days=1)
    str_yesterday = str(yesterday)

    try:
        tune_v3_logs_advertisers_clicks_export.collect(
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

    for row in list(tune_v3_logs_advertisers_clicks_export.generator):
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
