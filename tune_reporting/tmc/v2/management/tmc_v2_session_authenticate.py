#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @namespace tune_reporting
"""TUNE MobileAppTracking API base class
"""

import logging

from pyhttpstatus_utils import (HttpStatusType, is_http_status_type)
from tune_reporting.errors import (print_traceback, get_exception_message)
from tune_reporting.exceptions import (TuneReportingError)
from tune_reporting.support import (python_check_version)
from tune_reporting import (__python_required_version__)
from tune_reporting.tmc.tune_mobileapptracking_api_base import (TuneMobileAppTrackingApiBase)
from logging_mv_integrations import (TuneLoggingFormat)

python_check_version(__python_required_version__)


# @brief TUNE Authentication Types ENUM
#
# @namespace tune_reporting.TuneV2AuthenticationTypes
class TuneV2AuthenticationTypes(object):
    """TUNE Authentication Types ENUM
    """
    API_KEY = "api_key"
    SESSION_TOKEN = "session_token"

    @staticmethod
    def validate(auth_type):
        return auth_type in [TuneV2AuthenticationTypes.API_KEY, TuneV2AuthenticationTypes.SESSION_TOKEN]


# @brief  TUNE MobileAppTracking API v2/session/authenticate
#
# @namespace tune_reporting.TuneV2SessionAuthenticate
class TuneV2SessionAuthenticate(TuneMobileAppTrackingApiBase):
    """TUNE MobileAppTracking API v2/session/authenticate
    """

    # Initialize Job
    #
    def __init__(self, logger_level=logging.NOTSET, logger_format=TuneLoggingFormat.JSON):
        super(TuneV2SessionAuthenticate, self).__init__(logger_level=logger_level, logger_format=logger_format)

    def get_session_token(self, tmc_api_key, request_retry=None):
        """Generate session token is returned to provide
        access to service.

        Args:
            tmc_api_key:
            request_retry:

        Returns:

        """
        self.logger.info("TMC v2 /session/authenticate/: Get Token")

        self.api_key = tmc_api_key

        request_url = \
            self.tune_mat_request_path(
                mat_api_version="v2",
                controller="session/authenticate",
                action="api_key"
            )

        request_params = \
            {
                'api_keys': tmc_api_key,
                "source": "multiverse"
            }

        try:
            response = self.mv_request.request(
                request_method="GET",
                request_url=request_url,
                request_params=request_params,
                request_retry=None,
                request_retry_http_status_codes=None,
                request_retry_func=self.tune_v2_request_retry_func,
                request_retry_excps_func=None,
                request_label="TMC v2 Session Authenticate"
            )

        except TuneReportingError as tmv_ex:
            self.logger.error("TMC v2 /session/authenticate/: Failed: {}".format(str(tmv_ex)))
            raise

        except Exception as ex:
            print_traceback(ex)

            self.logger.error("TMC v2 /session/authenticate/: Failed: {}".format(get_exception_message(ex)))

            raise TuneReportingError(
                error_message=("TMC v2 /session/authenticate/: Failed: {}").format(get_exception_message(ex)),
                errors=ex
            )

        json_response = self.mv_request.validate_json_response(
            response, request_label="TMC v2 Get Session Token: Validate"
        )

        self.logger.debug("TuneV2SessionAuthenticate", extra={'response': json_response})

        json_response_status_code = json_response['status_code']
        http_status_successful = is_http_status_type(
            http_status_code=json_response_status_code, http_status_type=HttpStatusType.SUCCESSFUL
        )

        if not http_status_successful or not json_response['data']:
            raise TuneReportingError(error_message="Failed to authenticate: {}".format(json_response_status_code))

        self.session_token = json_response['data']

        self.logger.info("TuneV2SessionAuthenticate", extra={'session_token': self.session_token})

        self.logger.info("TMC v2 /session/authenticate/: Finished")

        return True
