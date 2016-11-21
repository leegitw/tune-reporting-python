#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @namespace tune_reporting
"""
TUNE Multiverse Reporting Base
================================
"""

import logging
from requests_mv_integrations.support import (
    base_class_name
)
from requests_mv_integrations.errors import (
    get_exception_message,
    print_traceback,
    ModuleAuthenticationError
)
from tune_reporting.errors import (
    TuneReportingError
)
from tune_reporting.tmc.v2.management.tmc_v2_session_authenticate import (
    TuneV2SessionAuthenticate
)
from logging_mv_integrations import (
    TuneLoggingFormat
)

log = logging.getLogger(__name__)


def tmc_auth_v2_session_token(
    tmc_api_key,
    logger_level=logging.NOTSET,
    logger_format=TuneLoggingFormat.JSON
):
    """TMC Authentication

    :return:
    """
    log.info(
        "TMC v2 /session/authenticate/: Request"
    )

    response_auth = None

    try:
        tune_v2_session_authenticate = \
            TuneV2SessionAuthenticate(
                logger_level=logger_level,
                logger_format=logger_format
            )

        if tune_v2_session_authenticate.get_session_token(
            tmc_api_key=tmc_api_key,
            request_retry=None
        ):
            session_token = tune_v2_session_authenticate.session_token

    except TuneReportingError as auth_ex:
        log.error(
            "TMC v2 /session/authenticate/: Failed",
            extra=auth_ex.to_dict()
        )

        raise

    except Exception as ex:
        print_traceback(ex)
        log.error(
            'TMC v2 Session Authenticate: Failed: Unexpected',
            extra={
                'error_exception': base_class_name(ex),
                'error_details': get_exception_message(ex)
            }
        )

        raise ModuleAuthenticationError(
            error_message="TMC v2 Session Authenticate: Failed: Unexpected",
            errors=ex
        )

    log.debug(
        "TMC v2 /session/authenticate/: Response",
        extra={
            'session_token': session_token
        }
    )

    return session_token