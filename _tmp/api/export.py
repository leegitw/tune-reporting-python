"""export.py
"""
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

from _tmp.base import (
    EndpointBase
)


## TUNE Reporting API endpoint '/export'
#
class Export(EndpointBase):
    """TUNE Reporting API endpoint '/export/'."""

    ## The constructor.
    #
    def __init__(self):
        """The constructor.
        """

        EndpointBase.__init__(
            self,
            controller="export",
            use_config=True
        )

    ## TuneManagementRequest status from export queue for report.
    #  When completed, url will be provided for downloading report.
    #
    #  @param str job_id   Job identifier assigned for report export.
    #  @return object @see TuneServiceResponse
    def download(self,
                 job_id):
        """
        Action 'download' for polling export queue for status information on
        request report to be exported.

            :param str job_id:   Job identifier assigned for report export.
            :return: TuneServiceResponse
        """
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        return EndpointBase.call(
            self,
            action="download",
            map_query_string={
                'job_id': job_id
            }
        )

    ## Helper function for fetching report upon completion.
    #  Starts worker for polling export queue.
    #
    #  @param str   job_id      Job identifier assigned for report export.
    #  @return object Document contents
    def fetch(self,
              job_id):
        """Helper function for fetching report upon completion.
        Starts worker for polling export queue.

            :param str  job_id:     Job identifier assigned for report export.
            :return:   Document contents
        """
        if not job_id or len(job_id) < 1:
            raise ValueError("Parameter 'job_id' is not defined.")

        return self._fetch(
            "export",
            "download",
            job_id
        )

    ## Helper function for parsing export status response to gather report url.
    #  @param @see TuneServiceResponse
    #  @return str Report Url
    @staticmethod
    def parse_response_report_url(response):
        """Helper function for parsing export status response to
        gather report url.

            :param object response: TuneServiceResponse
            :return (str): Report Url
            :throws: TuneSdkException
        """
        if not response:
            raise ValueError("Parameter 'response' is not defined.")
        if not response.data:
            raise ValueError("Parameter 'response.data' is not defined.")
        if "data" not in response.data:
            raise ValueError(
                "Parameter 'response.data['data'] is not defined."
            )
        if "url" not in response.data["data"]:
            raise ValueError(
                "Parameter 'response.data['data']['url'] is not defined."
            )

        url = response.data["data"]["url"]

        if sys.version_info >= (3, 0, 0):
            # for Python 3
            if isinstance(url, bytes):
                url = url.decode('ascii')  # or  s = str(s)[2:-1]
        else:
            if isinstance(url, unicode):
                url = str(url)

        return url
