#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)

import os
import sys
import logging
from pprintpp import pprint

from tune_reporting.exceptions import (TuneReportingError)
from requests_mv_integrations.exceptions import (TuneRequestBaseError)
from tune_reporting.errors import (print_traceback, get_exception_message)
from tune_reporting.tmc.v2.management import (TuneV2SessionAuthenticate)


def main(tmc_api_key):
    tune_v2_session_authenticate = \
        TuneV2SessionAuthenticate(
            logger_level=logging.INFO
        )

    try:
        if tune_v2_session_authenticate.get_session_token(
            tmc_api_key=tmc_api_key,
            request_retry=None
        ):
            session_token = tune_v2_session_authenticate.session_token
            print(session_token)

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
        tmc_api_key = os.environ.get('TMC_API_KEY')
        if tmc_api_key is None:
            if len(sys.argv) < 2:
                raise ValueError("{} [tmc_api_key].".format(sys.argv[0]))
            tmc_api_key = sys.argv[1]
            pprint("Argument: TMC API-KEY")
        else:
            pprint("Environment: TMC API-KEY")

        if tmc_api_key is None:
            raise ValueError("Missing: TMC API-KEY")
        sys.exit(main(tmc_api_key))
    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise
