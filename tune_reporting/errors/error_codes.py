#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @namespace tune_reporting.errors

from requests_mv_integrations.errors import (TuneRequestErrorCodes)


class TuneReportingErrorCodes(TuneRequestErrorCodes):
    """TUNE Reporting Error Codes
    """

    REP_ERR_UNASSIGNED = -1

    MOD_OK = 0  # Success

    #
    # 7xx Integration Module Errors
    #
    REP_ERR_MODULE = 700  # Module Error

    REP_ERR_CONFIG = 701
    # Exit code that means that some kind of configuration
    # error occurred.

    REP_ERR_ARGUMENT = 702
    # Invalid or missing argument provided.

    REP_ERR_ACCESS = 703
    # Exit code that means a user
    # specified access issues.

    REP_ERR_IO = 704
    # Exit code that means that an error
    # occurred while doing I/O on some file.

    REP_ERR_NOINPUT = 705
    # Exit code that means an input
    # file did not exist or was not readable.

    REP_ERR_NOPERM = 706
    # Exit code that means that there were insufficient
    # permissions to perform the operation (but not
    # intended for file system problems).

    REP_ERR_REQUEST = 707
    # Exit code that request failed.

    REP_ERR_SOFTWARE = 708
    # Exit code that means an internal
    # software error was detected.

    REP_ERR_INVALID_USAGE = 709
    # Exit code that means the command
    # was used incorrectly, such as when the
    # wrong number of arguments are given.

    REP_ERR_UNEXPECTED_VALUE = 710
    # Unexpected value either
    # returned or null.

    REP_ERR_UNEXPECTED_EXIT = 711
    # Integration ended unexpectedly and thereby no exit code was properly determined.

    REP_ERR_AMBIGUOUS = 712
    # There was an ambiguous exception that occurred while handling your request.

    REP_ERR_REQUEST_HTTP = 713
    # An HTTP error occurred.

    REP_ERR_REQUEST_CONNECT = 714
    # A Connection error occurred.

    REP_ERR_REQUEST_REDIRECTS = 715
    REP_ERR_INCOMPLETE_READ = 716
    REP_ERR_CHUNKED_ENCODING = 717
    REP_ERR_DATA_INVALID = 718  # Data not valid

    REP_ERR_SERVICE_UNAVAILABLE = 720  # Service Unavailable
    REP_ERR_JOB_STOPPED = 721  # Job Stopped
    REP_ERR_RETRY_EXHAUSTED = 722  # Retry Exhausted
    REP_ERR_UNEXPECTED_CONTENT_TYPE_RETURNED = 723  # Unexpected content-type returned

    REP_ERR_PAYLOAD_READ = 730
    REP_ERR_PAYLOAD_NOT_FOUND = 731
    REP_ERR_CONFIG_S3_URL_EXPIRED = 732

    REP_ERR_COLLECT_DATA = 740  # Error during data collection
    REP_ERR_UPLOAD_DATA = 741  # Error during data upload
    REP_ERR_INTEGRATION = 742  # Error during integration

    REP_ERR_RUN_TIMEOUT = 750  # Timeout error during data collection
    REP_ERR_RUNTIME_ERROR = 751  # Runtime error during data collection
    REP_ERR_RUN_STOPPED = 752  # Stopped error during data collection

    REP_ERR_AUTH_ERROR = 760  # Auth Error
    REP_ERR_AUTH_JSON_ERROR = 761  # Auth JSON Error
    REP_ERR_AUTH_RESP_ERROR = 762  # Auth Response Error
    REP_ERR_AUTH_MISSING_PARAMS = 763  # Auth Missing Parameters
    REP_ERR_AUTH_INVALID_PARAMS = 764  # Auth Invalid Parameters
    REP_ERR_OAUTH_CREDS_EXPIRED = 765  # OAuth Credentials expired

    REP_ERR_JSON_DECODING = 766  # JSON Decoding Error

    REP_ERR_UNEXPECTED = 799  # Unexpected Error
