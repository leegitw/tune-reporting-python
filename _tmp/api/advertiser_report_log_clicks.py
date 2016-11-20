"""
TUNE Reporting API '/advertiser/stats/clicks/'
================================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  advertiser_report_log_clicks.py
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


#  /advertiser/stats/clicks
#
#  @example example_reports_clicks.py
#
class AdvertiserReportLogClicks(AdvertiserReportLogBase):
    """TUNE Reporting API endpoint '/advertiser/stats/clicks'
    """

    ## The constructor.
    #
    def __init__(self):
        """The constructor.
        """
        AdvertiserReportLogBase.__init__(
            self,
            "advertiser/stats/clicks",
            True,
            True
        )

        self.fields_recommended = [
            "id",
            "created",
            "site_id",
            "site.name",
            "publisher_id",
            "publisher.name",
            "is_unique",
            "advertiser_sub_campaign_id",
            "advertiser_sub_campaign.ref",
            "publisher_sub_campaign_id",
            "publisher_sub_campaign.ref"
        ]
