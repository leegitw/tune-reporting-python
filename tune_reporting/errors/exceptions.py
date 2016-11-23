#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @namespace tune_reporting
"""
Tune Reporting Error
"""

from requests_mv_integrations.errors import (RequestErrorCode)
from requests_mv_integrations.errors.exceptions import (RequestBaseError)


class TuneReportingBaseError(RequestBaseError):
    pass


class TuneReportingError(TuneReportingBaseError):
    pass


class TuneReportingAuthError(TuneReportingBaseError):
    def __init__(self, **kwargs):
        error_code = kwargs.pop('error_code', None) or RequestErrorCode.MOD_ERR_AUTH_ERROR
        super(TuneReportingAuthError, self).__init__(error_code=error_code, **kwargs)
