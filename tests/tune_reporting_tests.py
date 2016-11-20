#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2016 TUNE, Inc.
#  All rights reserved.
#
#  Python 2.7 and 3.0
#
#  @category  Tune_Reporting
#  @package   Tune_Reporting_Python
#  @author    Jeff Tanner <jefft@tune.com>
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @license   http://opensource.org/licenses/MIT The MIT License (MIT)
#  @link      https://developers.tune.com @endlink
#

import sys
import unittest

from test_advertiser_report_log_clicks import TestAdvertiserReportLogClicks
from test_advertiser_report_log_event_items import TestAdvertiserReportLogEventItems
from test_advertiser_report_log_events import TestAdvertiserReportLogEvents
from test_advertiser_report_log_installs import TestAdvertiserReportLogInstalls
from test_advertiser_report_log_postbacks import TestAdvertiserReportLogPostbacks
from test_advertiser_report_actuals import TestAdvertiserReportActuals
from test_advertiser_report_cohort_retention import TestAdvertiserReportCohortRetention
from test_advertiser_report_cohort_values import TestAdvertiserReportCohortValues

def suite(api_key):
    suite = unittest.TestSuite()

    suite.addTest(TestAdvertiserReportLogClicks(api_key))
    suite.addTest(TestAdvertiserReportLogEventItems(api_key))
    suite.addTest(TestAdvertiserReportLogEvents(api_key))
    suite.addTest(TestAdvertiserReportLogInstalls(api_key))
    suite.addTest(TestAdvertiserReportLogPostbacks(api_key))
    suite.addTest(TestAdvertiserReportActuals(api_key))
    suite.addTest(TestAdvertiserReportCohortRetention(api_key))
    suite.addTest(TestAdvertiserReportCohortValues(api_key))

    return suite

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            api_key = sys.argv.pop()

    except Exception as exc:
        print("Exception: {0}".format(exc))
        raise

    runner = unittest.TextTestRunner()

    test_suite = suite(api_key)

    runner.run(test_suite)
