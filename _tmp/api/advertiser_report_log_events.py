"""
TUNE Reporting API '/advertiser/stats/events/'
====================================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  advertiser_report_log_events.py
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


#  /advertiser/stats/events
#  @example example_reports_events.py
class AdvertiserReportLogEvents(AdvertiserReportLogBase):
    """Advertiser Stats logs pertaining to events."""

    ## The constructor.
    #
    def __init__(self):
        """The constructor.
        """
        AdvertiserReportLogBase.__init__(
            self,
            "advertiser/stats/events",
            True,
            True
        )

        self.fields_recommended = [
            "id",
            "stat_install_id",
            "created",
            "status",
            "site_id",
            "site.name",
            "site_event_id",
            "site_event.name",
            "site_event.type",
            "publisher_id",
            "publisher.name",
            "advertiser_ref_id",
            "advertiser_sub_campaign_id",
            "advertiser_sub_campaign.ref",
            "publisher_sub_campaign_id",
            "publisher_sub_campaign.ref",
            "user_id",
            "device_id",
            "os_id",
            "google_aid",
            "ios_ifa",
            "ios_ifv",
            "windows_aid",
            "referral_url",
            "is_view_through",
            "is_reengagement"
        ]
