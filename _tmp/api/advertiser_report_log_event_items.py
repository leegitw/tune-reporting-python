"""
TUNE Reporting API '/advertiser/stats/event/items/'
====================================================
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  advertiser_report_log_event_items.py
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


#  /advertiser/stats/event/items
#  @example example_reports_event_items.py
class AdvertiserReportLogEventItems(AdvertiserReportLogBase):
    """Advertiser Stats logs pertaining to event items."""

    ## The constructor.
    #
    def __init__(self):
        """The constructor.
        """
        AdvertiserReportLogBase.__init__(
            self,
            "advertiser/stats/event/items",
            False,
            True
        )

        self.fields_recommended = [
            "id",
            "created",
            "site_id",
            "site.name",
            "campaign_id",
            "campaign.name",
            "site_event_id",
            "site_event.name",
            "site_event_item_id",
            "site_event_item.name",
            "quantity",
            "value_usd",
            "country_id",
            "country.name",
            "region_id",
            "region.name",
            "agency_id",
            "agency.name",
            "advertiser_sub_site_id",
            "advertiser_sub_site.name",
            "advertiser_sub_campaign_id",
            "advertiser_sub_campaign.name",
            "currency_code",
            "value"
        ]
