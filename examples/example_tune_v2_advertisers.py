#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)

import sys
import logging
from pprintpp import pprint

from requests_mv_integrations.exceptions import (TuneRequestBaseError)
from tune_reporting.errors import (print_traceback, get_exception_message)
from tune_reporting.exceptions import (TuneReportingError)
from tune_reporting.tmc.v2.management.tmc_v2_advertisers import (TuneV2Advertisers)
from tune_reporting.tmc.v2.management.tmc_v2_session_authenticate import (TuneV2AuthenticationTypes)
from logging_mv_integrations import (TuneLoggingFormat)


def main(tmc_api_key):
    tune_v2_advertisers = TuneV2Advertisers(logger_level=logging.DEBUG, logger_format=TuneLoggingFormat.JSON)

    try:
        tune_v2_advertisers.tmc_auth(tmc_api_key=tmc_api_key)

        if tune_v2_advertisers.get_advertiser_id(
            auth_value=tmc_api_key, auth_type=TuneV2AuthenticationTypes.API_KEY, request_retry=None
        ):
            advertiser_id = tune_v2_advertisers.advertiser_id
            pprint(advertiser_id)

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
