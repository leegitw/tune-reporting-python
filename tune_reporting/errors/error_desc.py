#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @namespace tune_reporting.errors

from requests_mv_integrations.errors import error_name as tune_requests_error_name
from requests_mv_integrations.errors import error_desc as tune_requests_error_desc

tune_reporting_error_name = {
    700: 'Module Error',
    701: 'Configuration Error',
    702: 'Argument Error',
    703: 'Access Error',
    704: 'I/O Error',
    705: 'No Input',
    706: 'No Permissions',
    707: 'Request Error',
    708: 'Software Error',
    709: 'Invalid Usage',
    710: 'Unexpected Value',
    711: 'Unexpected Exit',
    712: 'Request Ambiguous Error',
    713: 'Request HTTP',
    714: 'Request Connect',
    715: 'Request Redirect',
    716: 'Response Incomplete Read',
    717: 'Response Chuncked Encoding',
    718: 'Response Data Invalid',
    720: 'Retry Exhausted',
    721: 'Service Unavailable',
    722: 'Job Stopped',
    723: 'Unexpected content-type returned',
    730: 'Payload Read',
    731: 'Payload Not Found',
    732: 'AWS S3 URL Expired',
    740: 'Collect Data Error',
    741: 'Upload Data Error',
    742: 'Integration Error',
    750: 'Run Timeout Error',
    751: 'Runtime Error',
    752: 'Run Stopped Error',
    760: 'Auth Error',
    761: 'Auth JSON Error',
    762: 'Auth Response Error',
    763: 'Auth Missing Parameters',
    764: 'Auth Invalid Parameters',
    765: 'OAuth Credentials Expired',
    766: 'JSON Decoding Error',
    799: 'Unexpected Error'
}

tune_reporting_error_description = {
    -1: 'Unassiged exit condition',
    0: 'Successfully completed',
    700: 'Error occurred somewhere within module',
    701: 'Configuration Error',
    702: 'Invalid or missing argument provided',
    703: 'User has access issues',
    704: 'Error occurred while doing I/O on some file',
    705: 'Input file did not exist or was not readable',
    706: 'Insufficient permissions to perform the operation',
    707: 'Unexpected request failure',
    708: 'Unexpected software error was detected',
    709: 'Command was used incorrectly, such as when the wrong number of arguments are given',
    710: 'Unexpected value returned',
    711: 'Integration ended unexpectedly and thereby no exit code was properly determined',
    712: 'There was an ambiguous exception that occurred while handling your request',
    713: 'Request HTTP error occurred',
    714: 'Request Connection error occurred',
    715: 'Request Redirect',
    716: 'Response Incomplete Read',
    717: 'Response Chuncked Encoding',
    718: 'Response Data Invalid',
    720: 'Retry Exhausted',
    721: 'Service Unavailable',
    722: 'Job Stopped',
    723: 'Unexpected content-type returned',
    730: 'Payload Read',
    731: 'Payload Not Found',
    732: 'AWS S3 URL Expired',
    740: 'Collect Data Error',
    741: 'Upload Data Error',
    742: 'Integration Error',
    750: 'Timeout error during data collection',
    751: 'Runtime error during data collection',
    752: 'Stopped error during data collection',
    760: 'Auth Error',
    761: 'Auth JSON Error',
    762: 'Auth Response Error',
    763: 'Auth Missing Parameters',
    764: 'Auth Invalid Parameters',
    765: 'OAuth Credentials expired (refresh token likely invalid)',
    766: 'JSON Decoding Error',
    799: 'Unexpected Error'
}


def error_name(error_code):
    """Provide definition of Error Code

    Args:
        error_code:

    Returns:

    """
    if error_code is None or not isinstance(error_code, int):
        return "Error Code: Invalid Type: {}".format(error_code)

    error_code_name_ = tune_requests_error_name(error_code, return_bool=True)
    if error_code_name_ and error_code_name_ is not None:
        return error_code_name_

    error_code_name_ = tune_reporting_error_name.get(error_code, None)
    if error_code_name_ is not None:
        return error_code_name_

    return "Error Code: Undefined: {}".format(error_code)


def error_desc(error_code):
    """Provide definition of Error Code

    Args:
        error_code:

    Returns:

    """
    if error_code is None or not isinstance(error_code, int):
        return "Error Code: Invalid Type: {}".format(error_code)

    error_code_description_ = tune_requests_error_desc(error_code, return_bool=True)
    if error_code_description_ and error_code_description_ is not None:
        return error_code_description_

    error_code_description_ = tune_reporting_error_description.get(error_code, None)
    if error_code_description_ is not None:
        return error_code_description_

    return "Error Code: Undefined: {}".format(error_code)
