"""session_authenticate.py
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

from _tmp.base import (
    EndpointBase
)

## TUNE Reporting API endpoint '/session/authenticate'
#
class SessionAuthenticate(EndpointBase):
    """TUNE Reporting API endpoint '/session/authenticate/'."""

    ## The constructor.
    #
    def __init__(self):
        """The constructor.
        """

        EndpointBase.__init__(
            self,
            controller="session/authenticate",
            use_config=False
        )

    ## Generate session token is returned to provide access to service.
    #
    #  @param string api_keys  Generate 'session token' for this api_keys.
    #  @return object @see TuneServiceResponse
    def api_key(self,
                api_keys):
        """
        Generate session token is returned to provide access to service.

            :param api_keys (string):   Generate 'session token'
                                        for this api_keys.
            :return: TuneServiceResponse
        """
        if not api_keys or len(api_keys) < 1:
            raise ValueError("Parameter 'api_keys' is not defined.")

        return EndpointBase.call(
            self,
            action="api_key",
            map_query_string={
                'api_keys': api_keys
            }
        )
