#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  advertiser_report_actuals.py
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
"""
TUNE Reporting API '/advertiser/stats/'
====================================================
"""



#  /advertiser/stats
#  @example example_reports_actuals.py
class AdvertiserReportActuals(AdvertiserReportActualsBase):
    """
    TUNE Reporting API endpoint '/advertiser/stats/'
    """

    ## The constructor.
    #
    def __init__(self):
        """The constructor.
        """
        AdvertiserReportActualsBase.__init__(
            self,
            "advertiser/stats",
            True,
            True
        )

        self.fields_recommended = [
            "site_id",
            "site.name",
            "publisher_id",
            "publisher.name",
            "ad_impressions",
            "ad_impressions_unique",
            "ad_clicks",
            "ad_clicks_unique",
            "paid_installs",
            "paid_installs_assists",
            "non_installs_assists",
            "paid_events",
            "paid_events_assists",
            "non_events_assists",
            "paid_opens",
            "paid_opens_assists",
            "non_opens_assists"
        ]
