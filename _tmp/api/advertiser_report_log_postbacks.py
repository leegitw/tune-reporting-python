"""
TUNE Reporting API '/advertiser/stats/postbacks/'
====================================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  advertiser_report_log_postbacks.py
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

from _tmp.base import (
    AdvertiserReportLogBase
)


#  /advertiser/stats/postbacks
#  @example example_reports_postbacks.py
class AdvertiserReportLogPostbacks(AdvertiserReportLogBase):
    """Advertiser Stats logs pertaining to postbacks."""

    ## The constructor.
    #
    def __init__(self):
        """The constructor.
        """
        AdvertiserReportLogBase.__init__(
            self,
            "advertiser/stats/postbacks",
            False,
            True
        )

        self.fields_recommended = [
            "id",
            "stat_install_id",
            "stat_event_id",
            "stat_open_id",
            "created",
            "status",
            "site_id",
            "site.name",
            "site_event_id",
            "site_event.name",
            "site_event.type",
            "publisher_id",
            "publisher.name",
            "attributed_publisher_id",
            "attributed_publisher.name",
            "url",
            "http_result"
        ]
