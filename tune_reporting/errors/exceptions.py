#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @namespace tune_reporting
"""
Tune Reporting Error
"""

from requests_mv_integrations.errors import (TuneIntegrationBaseError)


class TuneReportingError(TuneIntegrationBaseError):
    pass
